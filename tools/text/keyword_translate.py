#!/usr/bin/env python3
"""Extract and rebuild the flat string table in KEYWORD.DAT."""

from __future__ import annotations

import argparse
import json
import struct
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "font"))
from build_font import encode_string  # noqa: E402

_DEFAULT_MAPPING = (
    Path(__file__).resolve().parents[2] / "localization" / "generated" / "zh_mapping.json"
)


def decode_keyword_dat(payload: bytes) -> list[str]:
    if len(payload) < 4:
        raise ValueError("KEYWORD.DAT is shorter than its header")
    declared_size, count = struct.unpack_from("<HH", payload)
    if declared_size != len(payload):
        raise ValueError(
            f"KEYWORD.DAT declares {declared_size} bytes, but contains {len(payload)}"
        )
    table_end = 4 + count * 2
    if table_end > len(payload):
        raise ValueError(f"KEYWORD.DAT offset table for {count} entries is truncated")

    strings: list[str] = []
    for index, (offset,) in enumerate(struct.iter_unpack("<H", payload[4:table_end]), 1):
        if offset < table_end or offset >= len(payload):
            raise ValueError(f"KEYWORD.DAT entry {index} has invalid offset {offset:#x}")
        end = payload.find(b"\0", offset)
        if end < 0:
            raise ValueError(f"KEYWORD.DAT entry {index} is not NUL terminated")
        strings.append(payload[offset:end].decode("latin1"))
    return strings


def encode_keyword_dat(strings: list[bytes]) -> bytes:
    table_end = 4 + len(strings) * 2
    pool = bytearray()
    offsets: list[int] = []
    interned: dict[bytes, int] = {}
    for value in strings:
        if b"\0" in value:
            raise ValueError("KEYWORD.DAT strings cannot contain NUL bytes")
        offset = interned.get(value)
        if offset is None:
            offset = table_end + len(pool)
            if offset > 0xFFFF:
                raise ValueError("KEYWORD.DAT string pool exceeds 16-bit offsets")
            interned[value] = offset
            pool += value + b"\0"
        offsets.append(offset)

    size = table_end + len(pool)
    if size > 0xFFFF:
        raise ValueError("KEYWORD.DAT exceeds its 16-bit size field")
    return struct.pack("<HH", size, len(strings)) + struct.pack(
        "<" + "H" * len(offsets), *offsets
    ) + pool


def _entry_id(index: int) -> str:
    return f"KEYWORD.DAT#{index}"


def cmd_scaffold(args: argparse.Namespace) -> None:
    strings = decode_keyword_dat(Path(args.keyword_path).read_bytes())
    out_path = Path(args.out) if args.out else Path("localization/translated/KEYWORD.json")
    existing: dict[str, dict[str, Any]] = {}
    if out_path.exists():
        prior = json.loads(out_path.read_text(encoding="utf-8"))
        existing = {entry["id"]: entry for entry in prior.get("entries", [])}

    entries = []
    drifted = []
    for index, source in enumerate(strings, 1):
        if not source:
            continue
        entry_id = _entry_id(index)
        old = existing.get(entry_id)
        if old is not None and old.get("source") != source:
            drifted.append(entry_id)
        entries.append(
            {
                "id": entry_id,
                "index": index,
                "source": source,
                "translation": old["translation"] if old else "",
                "status": old["status"] if old else "untranslated",
                "notes": old["notes"] if old else "",
            }
        )
    if drifted:
        print(f"warning: source drift in {len(drifted)} entries: {drifted[:10]}", file=sys.stderr)
    document = {
        "format": "BAK_ZH_KEYWORD_TRANSLATION",
        "version": 1,
        "source_file": "KEYWORD.DAT",
        "entry_count": len(strings),
        "entries": entries,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Scaffolded {len(entries)} non-empty entries from {len(strings)} slots to {out_path}")


def cmd_status(args: argparse.Namespace) -> None:
    document = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
    counts: dict[str, int] = {}
    for entry in document.get("entries", []):
        counts[entry["status"]] = counts.get(entry["status"], 0) + 1
    print(f"{document.get('source_file', '?')}: {len(document.get('entries', []))} entries")
    for status, count in sorted(counts.items()):
        print(f"  {status}: {count}")


def cmd_build(args: argparse.Namespace) -> None:
    source = decode_keyword_dat(Path(args.keyword_path).read_bytes())
    document = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
    translations = {entry["id"]: entry for entry in document.get("entries", [])}
    char_to_id = json.loads(Path(args.mapping).read_text(encoding="utf-8"))["char_to_id"]

    output: list[bytes] = []
    applied = drifted = 0
    for index, value in enumerate(source, 1):
        entry = translations.get(_entry_id(index))
        if not value or entry is None or entry.get("status") != "translated":
            output.append(value.encode("latin1"))
            continue
        if entry.get("source") != value:
            print(
                f"warning: {_entry_id(index)} source drift; keeping {value!r}", file=sys.stderr
            )
            output.append(value.encode("latin1"))
            drifted += 1
            continue
        translation = entry.get("translation", "")
        output.append(encode_string(translation, char_to_id) if translation else b"")
        applied += 1

    rebuilt = encode_keyword_dat(output)
    # Validate the generated table before committing it to disk.
    if len(decode_keyword_dat(rebuilt)) != len(source):
        raise AssertionError("rebuilt KEYWORD.DAT changed the slot count")
    Path(args.out).write_bytes(rebuilt)
    print(f"Built {args.out}: {applied} translated, {drifted} source-drift fallback(s)")


def main() -> None:
    parser = argparse.ArgumentParser(description="KEYWORD.DAT translation pipeline")
    sub = parser.add_subparsers(dest="cmd", required=True)

    scaffold = sub.add_parser("scaffold")
    scaffold.add_argument("keyword_path")
    scaffold.add_argument("--out")
    scaffold.set_defaults(func=cmd_scaffold)

    status = sub.add_parser("status")
    status.add_argument("json_path")
    status.set_defaults(func=cmd_status)

    build = sub.add_parser("build")
    build.add_argument("keyword_path")
    build.add_argument("json_path")
    build.add_argument("out")
    build.add_argument("--mapping", default=str(_DEFAULT_MAPPING))
    build.set_defaults(func=cmd_build)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
