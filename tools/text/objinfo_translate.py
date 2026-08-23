#!/usr/bin/env python3
"""
Betrayal at Krondor — OBJINFO.DAT Item-Name Translation Pipeline

OBJINFO.DAT (inside KRONDOR.RMF/.001) is a flat array of 138 fixed
80-byte ItemRecord structs (see upstream INCLUDE/structs.h), followed by
a 90-byte trailer table unrelated to text. Each record's first 32 bytes
are a NUL-padded item display name (ItemRecord.pName); the rest are
numeric gameplay fields left untouched by this tool.

Pipeline mirrors ddx_translate.py: scaffold -> fill in translations ->
build. Unlike DDX text, pName is a *fixed* 32-byte field, so a translated
name must encode to at most 31 bytes (room for the NUL terminator).
"""

from __future__ import annotations

import argparse
import json
import struct
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "font"))
from build_font import encode_string  # noqa: E402

RECORD_SIZE = 80
NAME_SIZE = 32
RECORD_COUNT = 138
TRAILER_SIZE = 90
EXPECTED_FILE_SIZE = RECORD_COUNT * RECORD_SIZE + TRAILER_SIZE

_DEFAULT_MAPPING = Path(__file__).resolve().parents[2] / "localization" / "generated" / "zh_mapping.json"


def _entry_id(index: int) -> str:
    return f"OBJINFO.DAT#{index}"


def _read_name(record: bytes) -> str:
    return record[:NAME_SIZE].split(b"\x00", 1)[0].decode("latin1")


def cmd_scaffold(args: argparse.Namespace) -> None:
    data = Path(args.objinfo_path).read_bytes()
    if len(data) != EXPECTED_FILE_SIZE:
        raise SystemExit(
            f"error: {args.objinfo_path} is {len(data)} bytes, expected {EXPECTED_FILE_SIZE} "
            f"({RECORD_COUNT} * {RECORD_SIZE} + {TRAILER_SIZE} trailer) -- refusing to scaffold "
            "against a file that doesn't match the known layout"
        )

    out_path = Path(args.out) if args.out else Path("localization/translated/OBJINFO.json")
    existing: dict[str, dict[str, Any]] = {}
    if out_path.exists():
        prior = json.loads(out_path.read_text(encoding="utf-8"))
        for e in prior.get("entries", []):
            existing[e["id"]] = e

    entries = []
    drifted = []
    for i in range(RECORD_COUNT):
        record = data[i * RECORD_SIZE:(i + 1) * RECORD_SIZE]
        name = _read_name(record)
        entry_id = _entry_id(i)
        if not name:
            continue
        prior_entry = existing.get(entry_id)
        if prior_entry is not None and prior_entry.get("source") != name:
            drifted.append(entry_id)
        entries.append({
            "id": entry_id,
            "index": i,
            "source": name,
            "translation": prior_entry["translation"] if prior_entry else "",
            "status": prior_entry["status"] if prior_entry else "untranslated",
            "notes": prior_entry["notes"] if prior_entry else "",
        })

    if drifted:
        print(f"warning: {len(drifted)} id(s) have a different source name than what's already on "
              f"file: {drifted[:10]}{' ...' if len(drifted) > 10 else ''}", file=sys.stderr)

    out_data = {
        "format": "BAK_ZH_OBJINFO_TRANSLATION",
        "version": 1,
        "source_file": "OBJINFO.DAT",
        "entries": entries,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out_data, indent=2, ensure_ascii=False), encoding="utf-8")

    added = sum(1 for e in entries if e["id"] not in existing)
    translated = sum(1 for e in entries if e["status"] == "translated")
    print(f"Scaffolded {len(entries)} entries ({added} new, {translated} already translated) to {out_path}")


def cmd_status(args: argparse.Namespace) -> None:
    data = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    by_status: dict[str, int] = {}
    for e in entries:
        by_status[e["status"]] = by_status.get(e["status"], 0) + 1
    print(f"{data.get('source_file', '?')}: {len(entries)} entries")
    for status, count in sorted(by_status.items()):
        print(f"  {status}: {count}")
    if args.show_untranslated:
        print("\nUntranslated:")
        for e in entries:
            if e["status"] != "untranslated":
                continue
            print(f"  {e['id']}: {e.get('source', '')!r}")


def cmd_build(args: argparse.Namespace) -> None:
    data = bytearray(Path(args.objinfo_path).read_bytes())
    if len(data) != EXPECTED_FILE_SIZE:
        raise SystemExit(
            f"error: {args.objinfo_path} is {len(data)} bytes, expected {EXPECTED_FILE_SIZE} -- "
            "refusing to build against a file that doesn't match the known layout"
        )
    translations = {
        e["id"]: e for e in json.loads(Path(args.json_path).read_text(encoding="utf-8")).get("entries", [])
    }
    char_to_id = json.loads(Path(args.mapping).read_text(encoding="utf-8"))["char_to_id"]

    applied = skipped_untranslated = skipped_too_long = skipped_source_drift = 0
    for i in range(RECORD_COUNT):
        offset = i * RECORD_SIZE
        record = data[offset:offset + RECORD_SIZE]
        name = _read_name(bytes(record))
        if not name:
            continue
        entry = translations.get(_entry_id(i))
        if entry is None or entry["status"] != "translated" or not entry["translation"]:
            continue
        if entry.get("source") != name:
            print(f"warning: {_entry_id(i)} source name on file ({entry.get('source')!r}) doesn't match "
                  f"the local OBJINFO.DAT ({name!r}); falling back to the local name", file=sys.stderr)
            skipped_source_drift += 1
            continue
        encoded = encode_string(entry["translation"], char_to_id)
        if len(encoded) > NAME_SIZE - 1:
            print(f"warning: {_entry_id(i)} translation {entry['translation']!r} encodes to "
                  f"{len(encoded)} bytes, exceeds the {NAME_SIZE - 1}-byte pName budget; "
                  "falling back to the English name", file=sys.stderr)
            skipped_too_long += 1
            continue
        padded = encoded + b"\x00" * (NAME_SIZE - len(encoded))
        data[offset:offset + NAME_SIZE] = padded
        # wName_split_off (offset 34, u16 LE -- ItemRecord.pName[32] is
        # immediately followed by wFlags at offset 32, THEN wName_split_off
        # at offset 34; do not overwrite wFlags). The English 2-line grid
        # split index no longer means anything against re-encoded bytes.
        # Chinese item names translated here are all short enough to render
        # on one grid line, so force single-line (0) rather than carry over
        # a stale byte offset into the new name.
        struct.pack_into("<H", data, offset + NAME_SIZE + 2, 0)
        applied += 1

    Path(args.out).write_bytes(bytes(data))
    print(f"Built {args.out}: {applied} name(s) translated, "
          f"{skipped_untranslated} marked-but-empty skipped, "
          f"{skipped_too_long} too-long fallback(s), "
          f"{skipped_source_drift} source-drift fallback(s)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Betrayal at Krondor OBJINFO.DAT item-name translation pipeline.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_scaffold = sub.add_parser("scaffold", help="Create/update a translation file from a local OBJINFO.DAT.")
    p_scaffold.add_argument("objinfo_path", help="Path to the local original OBJINFO.DAT file.")
    p_scaffold.add_argument("--out", help="Output JSON path (default: localization/translated/OBJINFO.json).")
    p_scaffold.set_defaults(func=cmd_scaffold)

    p_status = sub.add_parser("status", help="Show translation progress for a translation file.")
    p_status.add_argument("json_path", help="Path to the translation JSON file.")
    p_status.add_argument("--show-untranslated", action="store_true")
    p_status.set_defaults(func=cmd_status)

    p_build = sub.add_parser("build", help="Merge translations into a localized OBJINFO.DAT.")
    p_build.add_argument("objinfo_path", help="Path to the local original OBJINFO.DAT file.")
    p_build.add_argument("json_path", help="Path to the translation JSON file.")
    p_build.add_argument("out", help="Output path for the localized OBJINFO.DAT file.")
    p_build.add_argument("--mapping", default=str(_DEFAULT_MAPPING), help="Path to zh_mapping.json.")
    p_build.set_defaults(func=cmd_build)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
