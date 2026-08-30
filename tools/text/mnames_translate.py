#!/usr/bin/env python3
"""
Betrayal at Krondor -- MNAMES.DAT monster/creature-type name translation.

MNAMES.DAT (inside KRONDOR.RMF/.001) is the combat creature-type name table,
loaded by combatenc_mnames_lookup_dest() (SRC/COMBAT/ENC/CBENC.C). The combat
"assess enemy" dialogue (DDX records 0x84/0x85) sets
g_gameState.nEvtArgAux1 = actor->inner->creatureType and DIALOG.C case 17
expands an @-token by copying the matching MNAMES.DAT string into
g_speaker_names[slot] (a 32-byte buffer); every enemy combatant's .name field
is filled from the same table. The text renders through the DDX path, which
already handles the BAK-ZH double-byte encoding, so no engine change is needed.

Container format (identical in spirit to SPELLS.DAT):

    u16 count
    count * u16 offset          (into the string blob)
    u16 size field              (the shipped file stores the *total file size*
                                 here; the engine over-allocates and the read is
                                 bounded by EOF -- reproduced by setting the
                                 field to len(output))
    NUL-terminated string pool  (deduplicated: the 20-odd "INVALID MONSTER"
                                 placeholder slots all point at one string)

Rebuilt append-only: the original blob is kept byte-for-byte and translated
slots are repointed at freshly appended strings, so an all-untranslated build
reproduces the input exactly (asserted by `build`).

Pipeline mirrors objinfo_translate.py / spell_translate.py: scaffold -> fill in
translations -> build.
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

_DEFAULT_MAPPING = (
    Path(__file__).resolve().parents[2] / "localization" / "generated" / "zh_mapping.json"
)
_DEFAULT_JSON = (
    Path(__file__).resolve().parents[2] / "localization" / "translated" / "MNAMES.json"
)

# combatenc_mnames_lookup_dest strcpy's into g_speaker_names[slot], which is
# g_speaker_names[6][32]; leave room for the NUL.
NAME_BUDGET = 31
PLACEHOLDER = "INVALID MONSTER"


def decode_mnames_dat(payload: bytes) -> list[str]:
    if len(payload) < 2:
        raise ValueError("MNAMES.DAT is shorter than its header")
    (count,) = struct.unpack_from("<H", payload, 0)
    table_end = 2 + count * 2
    if table_end + 2 > len(payload):
        raise ValueError(f"MNAMES.DAT offset table for {count} entries is truncated")
    blob = payload[table_end + 2:]
    names: list[str] = []
    for i in range(count):
        (off,) = struct.unpack_from("<H", payload, 2 + i * 2)
        if off >= len(blob):
            raise ValueError(f"MNAMES.DAT entry {i} offset {off:#x} is out of range")
        end = blob.find(b"\0", off)
        if end < 0:
            raise ValueError(f"MNAMES.DAT entry {i} is not NUL terminated")
        names.append(blob[off:end].decode("latin1"))
    return names


def _entry_id(index: int) -> str:
    return f"MNAMES.DAT#{index}"


def cmd_scaffold(args: argparse.Namespace) -> None:
    names = decode_mnames_dat(Path(args.mnames_path).read_bytes())

    out_path = Path(args.out) if args.out else _DEFAULT_JSON
    existing: dict[str, dict[str, Any]] = {}
    if out_path.exists():
        for e in json.loads(out_path.read_text(encoding="utf-8")).get("entries", []):
            existing[e["id"]] = e

    entries = []
    drifted = []
    for i, name in enumerate(names):
        entry_id = _entry_id(i)
        prior = existing.get(entry_id)
        if prior is not None and prior.get("source") != name:
            drifted.append(entry_id)
        entries.append({
            "id": entry_id,
            "index": i,
            "source": name,
            "translation": prior["translation"] if prior else "",
            "status": prior["status"] if prior else "untranslated",
            "notes": prior["notes"] if prior else (
                "placeholder slot -- never displayed for a real creature"
                if name == PLACEHOLDER else ""
            ),
        })

    if drifted:
        print(f"warning: {len(drifted)} id(s) have a different source name than what's already "
              f"on file: {drifted[:10]}{' ...' if len(drifted) > 10 else ''}", file=sys.stderr)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({
        "format": "BAK_ZH_MNAMES_TRANSLATION",
        "version": 1,
        "source_file": "MNAMES.DAT",
        "entries": entries,
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    added = sum(1 for e in entries if e["id"] not in existing)
    translated = sum(1 for e in entries if e["status"] == "translated")
    real = sum(1 for e in entries if e["source"] != PLACEHOLDER)
    print(f"Scaffolded {len(entries)} entries ({real} real names, {added} new, "
          f"{translated} already translated) to {out_path}")


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
            if e["status"] != "untranslated" or e.get("source") == PLACEHOLDER:
                continue
            print(f"  {e['id']}: {e.get('source', '')!r}")


def cmd_build(args: argparse.Namespace) -> None:
    orig = Path(args.mnames_path).read_bytes()
    names = decode_mnames_dat(orig)
    count = len(names)
    table_end = 2 + count * 2
    offsets = list(struct.unpack_from("<" + "H" * count, orig, 2))
    blob = bytearray(orig[table_end + 2:])

    translations = {
        e["id"]: e
        for e in json.loads(Path(args.json_path).read_text(encoding="utf-8")).get("entries", [])
    }
    char_to_id = json.loads(Path(args.mapping).read_text(encoding="utf-8"))["char_to_id"]

    applied = skipped_too_long = skipped_source_drift = 0
    for i, name in enumerate(names):
        entry = translations.get(_entry_id(i))
        if entry is None or entry["status"] != "translated" or not entry["translation"]:
            continue
        if entry.get("source") != name:
            print(f"warning: {_entry_id(i)} source drift (file has {name!r}, json has "
                  f"{entry.get('source')!r}); keeping the local name", file=sys.stderr)
            skipped_source_drift += 1
            continue
        encoded = encode_string(entry["translation"], char_to_id)
        if len(encoded) > NAME_BUDGET:
            print(f"warning: {_entry_id(i)} translation {entry['translation']!r} encodes to "
                  f"{len(encoded)} bytes, exceeds the {NAME_BUDGET}-byte g_speaker_names budget; "
                  "keeping the English name", file=sys.stderr)
            skipped_too_long += 1
            continue
        new_off = len(blob)
        if new_off > 0xFFFF:
            print(f"warning: {_entry_id(i)} would push the string pool past a 16-bit offset; "
                  f"keeping {name!r}", file=sys.stderr)
            continue
        blob += encoded + b"\0"
        offsets[i] = new_off
        applied += 1

    out = bytearray()
    out += struct.pack("<H", count)
    out += struct.pack("<" + "H" * count, *offsets)
    size_field_at = len(out)
    out += struct.pack("<H", 0)
    out += blob
    struct.pack_into("<H", out, size_field_at, len(out) & 0xFFFF)
    out = bytes(out)

    # validate + round-trip guarantee
    if decode_mnames_dat(out) != _decode_after(names, translations, char_to_id):
        raise AssertionError("rebuilt MNAMES.DAT does not decode back to the expected names")
    if applied == 0 and out != orig:
        raise AssertionError("no translations applied but the rebuild differs from the input")

    Path(args.out).write_bytes(out)
    print(f"Built {args.out}: {applied} name(s) translated, "
          f"{skipped_too_long} too-long fallback(s), "
          f"{skipped_source_drift} source-drift fallback(s)")


def _decode_after(names: list[str], translations: dict, char_to_id: dict) -> list[str]:
    """The names the rebuilt file should decode to (English, except applied rows
    which become the raw-byte latin1 view of the encoded translation)."""
    out = []
    for i, name in enumerate(names):
        e = translations.get(_entry_id(i))
        if (e and e["status"] == "translated" and e["translation"]
                and e.get("source") == name):
            enc = encode_string(e["translation"], char_to_id)
            if len(enc) <= NAME_BUDGET:
                out.append(enc.decode("latin1"))
                continue
        out.append(name)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Betrayal at Krondor MNAMES.DAT creature-name translation pipeline."
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("scaffold", help="Create/update a translation file from a local MNAMES.DAT.")
    p.add_argument("mnames_path", help="Path to the local original MNAMES.DAT.")
    p.add_argument("--out", help=f"Output JSON path (default: {_DEFAULT_JSON}).")
    p.set_defaults(func=cmd_scaffold)

    p = sub.add_parser("status", help="Show translation progress.")
    p.add_argument("json_path")
    p.add_argument("--show-untranslated", action="store_true")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("build", help="Merge translations into a localized MNAMES.DAT.")
    p.add_argument("mnames_path", help="Path to the local original MNAMES.DAT.")
    p.add_argument("json_path", help="Path to the translation JSON file.")
    p.add_argument("out", help="Output path for the localized MNAMES.DAT.")
    p.add_argument("--mapping", default=str(_DEFAULT_MAPPING), help="Path to zh_mapping.json.")
    p.set_defaults(func=cmd_build)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
