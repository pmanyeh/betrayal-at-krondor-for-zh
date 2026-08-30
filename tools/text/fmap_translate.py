#!/usr/bin/env python3
"""
Betrayal at Krondor -- fmap_twn.dat world-map town-label translation.

fmap_twn.dat (inside KRONDOR.RMF/.001) holds the town-name labels drawn on the
travel map (SRC/SCREENS/FMAP.C: fmap_twn_load / the hover-label draw loop). It
is the simplest text container in the game -- a fixed header then a flat
sequence of length-prefixed records, with no offset table:

    u16 mapWidth
    u16 mapHeight
    u16 hotspotWidth
    u16 hotspotHeight
    u16 townCount
    townCount * { u16 strLen ; strLen bytes (name, NUL-terminated, strLen
                 counts the NUL) ; u16 x ; u16 y }

fmap_twn_load() galloc's exactly strLen bytes per label and reads strLen bytes,
so labels are free to grow or shrink -- this tool just rewrites each record with
a new strLen. Labels render through font_draw_text_ds / font_text_width_ds,
which already handle the BAK-ZH double-byte encoding, and font_text_width_ds
reports 16px per wide glyph so the auto-sized label rect width stays correct.
(The label-erase rect *height* is a separate engine concern -- see FMAP.C.)

Pipeline mirrors objinfo_translate.py / mnames_translate.py: scaffold -> fill in
translations -> build. A translated name must encode to <= 62 bytes so the
u16-plus-NUL record header stays sane; in practice every town name is far
shorter.
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
    Path(__file__).resolve().parents[2] / "localization" / "translated" / "FMAP_TWN.json"
)

HEADER = struct.Struct("<HHHHH")  # mapW, mapH, hotspotW, hotspotH, townCount
NAME_BUDGET = 62


def _iter_records(payload: bytes):
    if len(payload) < HEADER.size:
        raise ValueError("fmap_twn.dat is shorter than its header")
    mapw, maph, hotw, hoth, count = HEADER.unpack_from(payload, 0)
    pos = HEADER.size
    recs = []
    for i in range(count):
        if pos + 2 > len(payload):
            raise ValueError(f"fmap_twn.dat record {i} length field is truncated")
        (slen,) = struct.unpack_from("<H", payload, pos)
        pos += 2
        if pos + slen + 4 > len(payload):
            raise ValueError(f"fmap_twn.dat record {i} body/coords are truncated")
        raw = payload[pos:pos + slen]
        pos += slen
        x, y = struct.unpack_from("<HH", payload, pos)
        pos += 4
        recs.append({"raw": raw, "x": x, "y": y})
    if pos != len(payload):
        raise ValueError(
            f"fmap_twn.dat has {len(payload) - pos} trailing byte(s) after {count} records"
        )
    return (mapw, maph, hotw, hoth), recs


def decode_fmap_twn(payload: bytes) -> list[str]:
    _hdr, recs = _iter_records(payload)
    return [r["raw"].split(b"\0", 1)[0].decode("latin1") for r in recs]


def _entry_id(index: int) -> str:
    return f"FMAP_TWN.DAT#{index}"


def cmd_scaffold(args: argparse.Namespace) -> None:
    names = decode_fmap_twn(Path(args.fmap_path).read_bytes())
    _hdr, recs = _iter_records(Path(args.fmap_path).read_bytes())

    out_path = Path(args.out) if args.out else _DEFAULT_JSON
    existing: dict[str, dict[str, Any]] = {}
    if out_path.exists():
        for e in json.loads(out_path.read_text(encoding="utf-8")).get("entries", []):
            existing[e["id"]] = e

    entries = []
    drifted = []
    for i, (name, rec) in enumerate(zip(names, recs)):
        entry_id = _entry_id(i)
        prior = existing.get(entry_id)
        if prior is not None and prior.get("source") != name:
            drifted.append(entry_id)
        entries.append({
            "id": entry_id,
            "index": i,
            "source": name,
            "x": rec["x"],
            "y": rec["y"],
            "translation": prior["translation"] if prior else "",
            "status": prior["status"] if prior else "untranslated",
            "notes": prior["notes"] if prior else "",
        })

    if drifted:
        print(f"warning: {len(drifted)} id(s) have a different source name than what's already "
              f"on file: {drifted}", file=sys.stderr)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({
        "format": "BAK_ZH_FMAP_TWN_TRANSLATION",
        "version": 1,
        "source_file": "fmap_twn.dat",
        "entries": entries,
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    translated = sum(1 for e in entries if e["status"] == "translated")
    print(f"Scaffolded {len(entries)} town labels ({translated} already translated) to {out_path}")


def cmd_status(args: argparse.Namespace) -> None:
    data = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    by_status: dict[str, int] = {}
    for e in entries:
        by_status[e["status"]] = by_status.get(e["status"], 0) + 1
    print(f"{data.get('source_file', '?')}: {len(entries)} town labels")
    for status, count in sorted(by_status.items()):
        print(f"  {status}: {count}")
    if args.show_untranslated:
        for e in entries:
            if e["status"] == "untranslated":
                print(f"  {e['id']}: {e.get('source', '')!r}")


def cmd_build(args: argparse.Namespace) -> None:
    orig = Path(args.fmap_path).read_bytes()
    hdr, recs = _iter_records(orig)
    translations = {
        e["id"]: e
        for e in json.loads(Path(args.json_path).read_text(encoding="utf-8")).get("entries", [])
    }
    char_to_id = json.loads(Path(args.mapping).read_text(encoding="utf-8"))["char_to_id"]

    out = bytearray(HEADER.pack(*hdr, len(recs)))
    applied = skipped_too_long = skipped_source_drift = 0
    for i, rec in enumerate(recs):
        name = rec["raw"].split(b"\0", 1)[0].decode("latin1")
        entry = translations.get(_entry_id(i))
        body = rec["raw"]
        if entry is not None and entry["status"] == "translated" and entry["translation"]:
            if entry.get("source") != name:
                print(f"warning: {_entry_id(i)} source drift (file has {name!r}, json has "
                      f"{entry.get('source')!r}); keeping the local name", file=sys.stderr)
                skipped_source_drift += 1
            else:
                encoded = encode_string(entry["translation"], char_to_id) + b"\0"
                if len(encoded) > NAME_BUDGET:
                    print(f"warning: {_entry_id(i)} translation {entry['translation']!r} encodes to "
                          f"{len(encoded)} bytes (> {NAME_BUDGET}); keeping the English name",
                          file=sys.stderr)
                    skipped_too_long += 1
                else:
                    body = encoded
                    applied += 1
        out += struct.pack("<H", len(body))
        out += body
        out += struct.pack("<HH", rec["x"], rec["y"])

    out = bytes(out)
    # validate: re-parse cleanly and confirm the round-trip guarantee
    _iter_records(out)
    if applied == 0 and out != orig:
        raise AssertionError("no translations applied but the rebuild differs from the input")

    Path(args.out).write_bytes(out)
    print(f"Built {args.out}: {applied} label(s) translated, "
          f"{skipped_too_long} too-long fallback(s), "
          f"{skipped_source_drift} source-drift fallback(s)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Betrayal at Krondor fmap_twn.dat world-map town-label translation pipeline."
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("scaffold", help="Create/update a translation file from a local fmap_twn.dat.")
    p.add_argument("fmap_path", help="Path to the local original fmap_twn.dat.")
    p.add_argument("--out", help=f"Output JSON path (default: {_DEFAULT_JSON}).")
    p.set_defaults(func=cmd_scaffold)

    p = sub.add_parser("status", help="Show translation progress.")
    p.add_argument("json_path")
    p.add_argument("--show-untranslated", action="store_true")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("build", help="Merge translations into a localized fmap_twn.dat.")
    p.add_argument("fmap_path", help="Path to the local original fmap_twn.dat.")
    p.add_argument("json_path", help="Path to the translation JSON file.")
    p.add_argument("out", help="Output path for the localized fmap_twn.dat.")
    p.add_argument("--mapping", default=str(_DEFAULT_MAPPING), help="Path to zh_mapping.json.")
    p.set_defaults(func=cmd_build)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
