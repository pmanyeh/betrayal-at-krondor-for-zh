#!/usr/bin/env python3
"""
Betrayal at Krondor -- spell-text translation pipeline (SPELLS.DAT / SPELLDOC.DAT / INVSPELL.DAT)

Three resource files inside KRONDOR.RMF/.001 carry every piece of
player-visible spell text. All three are loaded by SRC/COMBAT/SPELL/CSPELL.C
(spells / spelldoc) and SRC/CHAR/CHARSCRN.C (invspell), and every string is
drawn through font_draw_text_ds / textwrap_draw_aligned, which already handle
the BAK-ZH double-byte encoding -- so no engine change is needed for the data
itself.

  SPELLS.DAT   u16 count
               count * SpellDef (22 bytes: u16 pName offset + 10 * i16 stats)
               u16 blob-length field (the shipped files store the *total file
                   size* here; the engine over-allocates and short-reads, so we
                   reproduce that: the field is set to len(output))
               NUL-terminated name string pool
               -> 45 spell names, shown in the combat cast menu.

  SPELLDOC.DAT u16 rowCount  (== spellCount * 7)
               rowCount * u32 offset into the blob
               u16 blob-length field (same total-file-size quirk)
               NUL-terminated string pool, with shared substrings: many rows
                   point at the same offset (blank lines, "Damage: None", ...),
                   and some offsets land on another string's trailing NUL.
               -> per spell: row 0 title, rows 1..6 description lines
                  (Cost / Damage / Duration / Line of sight / effect prose).
                  NOTE: cspell_info_panel_show() overrides rows 1-2 at runtime
                  with the computed "Cost: N Health+Stamina" / "Damage: N"
                  strings (hard-coded in CSPELL.C) for castable spells, so those
                  two English lines are handled separately in the source, not here.

  INVSPELL.DAT 6 school panels, each: u16 iconId, u16 count,
               count * { char name[24] (NUL padded); u16 spellIdx }
               -> the "spell book" list on the character screen. Fixed 24-byte
                  name field: a translation must encode to <= 23 bytes.

SPELLS.DAT / SPELLDOC.DAT are rebuilt append-only: the original string pool is
kept byte-for-byte and translated rows are repointed at freshly appended
strings. An all-untranslated build therefore reproduces the input exactly
(the build step asserts this). INVSPELL.DAT is patched in place like
OBJINFO.DAT.

Pipeline mirrors objinfo_translate.py / keyword_translate.py: scaffold -> fill
in translations -> build.
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
    Path(__file__).resolve().parents[2] / "localization" / "translated" / "SPELLS.json"
)

SPELLDEF_SIZE = 22
SPELLDOC_LINES = 7          # title + 6 description rows per spell
INVSPELL_NAME_SIZE = 24
INVSPELL_PANELS = 6
# alloc_far((long)(int)blobLen, 0) in cspell_subsystem_load sign-extends a
# 16-bit length; keep every rebuilt file safely below the point where that cast
# turns negative.
MAX_FILE_SIZE = 0x8000
# cspell_info_panel_show copies each doc row into a 60-byte line_buf via an
# unbounded strcpy; leave headroom.
SPELLDOC_LINE_BUDGET = 58


# --------------------------------------------------------------------------- #
# decoders
# --------------------------------------------------------------------------- #
def decode_spells_dat(payload: bytes) -> tuple[int, list[str]]:
    """Returns (spell count, list of spell names)."""
    if len(payload) < 2:
        raise ValueError("SPELLS.DAT is shorter than its header")
    (count,) = struct.unpack_from("<H", payload, 0)
    recs_end = 2 + count * SPELLDEF_SIZE
    if recs_end + 2 > len(payload):
        raise ValueError(f"SPELLS.DAT record table for {count} spells is truncated")
    blob_start = recs_end + 2
    blob = payload[blob_start:]
    names: list[str] = []
    for i in range(count):
        (off,) = struct.unpack_from("<H", payload, 2 + i * SPELLDEF_SIZE)
        if off >= len(blob):
            raise ValueError(f"SPELLS.DAT spell {i} name offset {off:#x} is out of range")
        end = blob.find(b"\0", off)
        if end < 0:
            raise ValueError(f"SPELLS.DAT spell {i} name is not NUL terminated")
        names.append(blob[off:end].decode("latin1"))
    return count, names


def decode_spelldoc_dat(payload: bytes) -> tuple[int, list[str]]:
    """Returns (row count, list of row strings)."""
    if len(payload) < 2:
        raise ValueError("SPELLDOC.DAT is shorter than its header")
    (rows,) = struct.unpack_from("<H", payload, 0)
    recs_end = 2 + rows * 4
    if recs_end + 2 > len(payload):
        raise ValueError(f"SPELLDOC.DAT offset table for {rows} rows is truncated")
    blob_start = recs_end + 2
    blob = payload[blob_start:]
    out: list[str] = []
    for i in range(rows):
        (off,) = struct.unpack_from("<I", payload, 2 + i * 4)
        if off >= len(blob):
            raise ValueError(f"SPELLDOC.DAT row {i} offset {off:#x} is out of range")
        end = blob.find(b"\0", off)
        if end < 0:
            raise ValueError(f"SPELLDOC.DAT row {i} string is not NUL terminated")
        out.append(blob[off:end].decode("latin1"))
    return rows, out


def decode_invspell_dat(payload: bytes) -> list[list[dict[str, Any]]]:
    """Returns 6 panels, each a list of {name, spell_idx, rec_off}."""
    panels: list[list[dict[str, Any]]] = []
    pos = 0
    for panel in range(INVSPELL_PANELS):
        if pos + 4 > len(payload):
            raise ValueError(f"INVSPELL.DAT panel {panel} header is truncated")
        _icon, count = struct.unpack_from("<HH", payload, pos)
        pos += 4
        recs: list[dict[str, Any]] = []
        for _ in range(count):
            if pos + INVSPELL_NAME_SIZE + 2 > len(payload):
                raise ValueError(f"INVSPELL.DAT panel {panel} record is truncated")
            raw = payload[pos:pos + INVSPELL_NAME_SIZE]
            (idx,) = struct.unpack_from("<H", payload, pos + INVSPELL_NAME_SIZE)
            recs.append({
                "name": raw.split(b"\0", 1)[0].decode("latin1"),
                "spell_idx": idx,
                "rec_off": pos,
            })
            pos += INVSPELL_NAME_SIZE + 2
        panels.append(recs)
    if pos != len(payload):
        raise ValueError(
            f"INVSPELL.DAT has {len(payload) - pos} trailing byte(s) after 6 panels"
        )
    return panels


# --------------------------------------------------------------------------- #
# entry ids
# --------------------------------------------------------------------------- #
def _spells_id(i: int) -> str:
    return f"SPELLS.DAT#{i}"


def _spelldoc_id(row: int) -> str:
    return f"SPELLDOC.DAT#{row // SPELLDOC_LINES}.{row % SPELLDOC_LINES}"


def _invspell_id(panel: int, slot: int) -> str:
    return f"INVSPELL.DAT#{panel}.{slot}"


# --------------------------------------------------------------------------- #
# scaffold
# --------------------------------------------------------------------------- #
def _merge_entry(existing: dict[str, dict], entry_id: str, source: str,
                 extra: dict[str, Any], drifted: list[str]) -> dict[str, Any]:
    prior = existing.get(entry_id)
    if prior is not None and prior.get("source") != source:
        drifted.append(entry_id)
    out = {
        "id": entry_id,
        "source": source,
        "translation": prior["translation"] if prior else "",
        "status": prior["status"] if prior else "untranslated",
        "notes": prior["notes"] if prior else "",
    }
    out.update(extra)
    return out


def cmd_scaffold(args: argparse.Namespace) -> None:
    _count, spell_names = decode_spells_dat(Path(args.spells).read_bytes())
    doc_rows, doc_strings = decode_spelldoc_dat(Path(args.spelldoc).read_bytes())
    panels = decode_invspell_dat(Path(args.invspell).read_bytes())

    if doc_rows != len(spell_names) * SPELLDOC_LINES:
        print(f"warning: SPELLDOC.DAT has {doc_rows} rows, expected "
              f"{len(spell_names) * SPELLDOC_LINES} ({len(spell_names)} spells * "
              f"{SPELLDOC_LINES})", file=sys.stderr)

    out_path = Path(args.out) if args.out else _DEFAULT_JSON
    existing: dict[str, dict] = {}
    if out_path.exists():
        for e in json.loads(out_path.read_text(encoding="utf-8")).get("entries", []):
            existing[e["id"]] = e

    drifted: list[str] = []
    entries: list[dict[str, Any]] = []

    for i, name in enumerate(spell_names):
        entries.append(_merge_entry(existing, _spells_id(i), name,
                                    {"file": "SPELLS.DAT", "index": i}, drifted))

    line_kind = ["title", "line1", "line2", "line3", "line4", "line5", "line6"]
    for row, text in enumerate(doc_strings):
        spell = row // SPELLDOC_LINES
        line = row % SPELLDOC_LINES
        extra = {
            "file": "SPELLDOC.DAT",
            "row": row,
            "spell": spell,
            "kind": line_kind[line],
            "spell_name": spell_names[spell] if spell < len(spell_names) else "",
        }
        entries.append(_merge_entry(existing, _spelldoc_id(row), text, extra, drifted))

    for panel, recs in enumerate(panels):
        for slot, rec in enumerate(recs):
            extra = {
                "file": "INVSPELL.DAT",
                "panel": panel,
                "slot": slot,
                "spell_idx": rec["spell_idx"],
            }
            entries.append(_merge_entry(existing, _invspell_id(panel, slot),
                                        rec["name"], extra, drifted))

    if drifted:
        print(f"warning: {len(drifted)} id(s) have a different source string than what's "
              f"already on file: {drifted[:10]}{' ...' if len(drifted) > 10 else ''}",
              file=sys.stderr)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({
        "format": "BAK_ZH_SPELL_TRANSLATION",
        "version": 1,
        "source_files": ["SPELLS.DAT", "SPELLDOC.DAT", "INVSPELL.DAT"],
        "entries": entries,
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    added = sum(1 for e in entries if e["id"] not in existing)
    translated = sum(1 for e in entries if e["status"] == "translated")
    print(f"Scaffolded {len(entries)} entries ({added} new, {translated} already translated) "
          f"to {out_path}")


# --------------------------------------------------------------------------- #
# status
# --------------------------------------------------------------------------- #
def cmd_status(args: argparse.Namespace) -> None:
    data = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    by_file: dict[str, dict[str, int]] = {}
    for e in entries:
        bucket = by_file.setdefault(e.get("file", "?"), {})
        bucket[e["status"]] = bucket.get(e["status"], 0) + 1
    print(f"{data.get('format', '?')}: {len(entries)} entries")
    for fname, buckets in by_file.items():
        total = sum(buckets.values())
        done = buckets.get("translated", 0)
        print(f"  {fname}: {done}/{total} translated")
        for status, count in sorted(buckets.items()):
            print(f"      {status}: {count}")
    if args.show_untranslated:
        print("\nUntranslated:")
        for e in entries:
            if e["status"] != "untranslated":
                continue
            print(f"  {e['id']}: {e.get('source', '')!r}")


# --------------------------------------------------------------------------- #
# build
# --------------------------------------------------------------------------- #
def _translated(entry: dict | None, source: str, ctx: str) -> str | None:
    """Return the translation to apply, or None to keep the source. Warns on drift."""
    if entry is None or entry.get("status") != "translated" or not entry.get("translation"):
        return None
    if entry.get("source") != source:
        print(f"warning: {ctx} source drift (file has {source!r}, json has "
              f"{entry.get('source')!r}); keeping the local string", file=sys.stderr)
        return None
    return entry["translation"]


def _build_spells(orig: bytes, tr: dict[str, dict], char_to_id: dict) -> tuple[bytes, int]:
    count, names = decode_spells_dat(orig)
    recs_end = 2 + count * SPELLDEF_SIZE
    blob = bytearray(orig[recs_end + 2:])
    records = bytearray(orig[2:recs_end])
    applied = 0
    for i, name in enumerate(names):
        zh = _translated(tr.get(_spells_id(i)), name, _spells_id(i))
        if zh is None:
            continue
        encoded = encode_string(zh, char_to_id)
        new_off = len(blob)
        if new_off > 0xFFFF:
            print(f"warning: {_spells_id(i)} would push the name pool past a 16-bit "
                  f"offset; keeping {name!r}", file=sys.stderr)
            continue
        blob += encoded + b"\0"
        struct.pack_into("<H", records, i * SPELLDEF_SIZE, new_off)
        applied += 1
    out = bytearray()
    out += struct.pack("<H", count)
    out += records
    size_field_at = len(out)
    out += struct.pack("<H", 0)  # placeholder
    out += blob
    struct.pack_into("<H", out, size_field_at, len(out) & 0xFFFF)
    return bytes(out), applied


def _build_spelldoc(orig: bytes, tr: dict[str, dict], char_to_id: dict) -> tuple[bytes, int]:
    rows, strings = decode_spelldoc_dat(orig)
    recs_end = 2 + rows * 4
    blob = bytearray(orig[recs_end + 2:])
    offsets = list(struct.unpack_from("<" + "I" * rows, orig, 2))
    applied = skipped_long = 0
    for row, text in enumerate(strings):
        eid = _spelldoc_id(row)
        zh = _translated(tr.get(eid), text, eid)
        if zh is None:
            continue
        encoded = encode_string(zh, char_to_id)
        if len(encoded) > SPELLDOC_LINE_BUDGET:
            print(f"warning: {eid} translation {zh!r} encodes to {len(encoded)} bytes, "
                  f"exceeds the {SPELLDOC_LINE_BUDGET}-byte line budget; keeping English",
                  file=sys.stderr)
            skipped_long += 1
            continue
        offsets[row] = len(blob)
        blob += encoded + b"\0"
        applied += 1
    out = bytearray()
    out += struct.pack("<H", rows)
    out += struct.pack("<" + "I" * rows, *offsets)
    size_field_at = len(out)
    out += struct.pack("<H", 0)
    out += blob
    struct.pack_into("<H", out, size_field_at, len(out) & 0xFFFF)
    if skipped_long:
        print(f"  SPELLDOC.DAT: {skipped_long} over-budget line(s) left in English")
    return bytes(out), applied


def _build_invspell(orig: bytes, tr: dict[str, dict], char_to_id: dict) -> tuple[bytes, int]:
    panels = decode_invspell_dat(orig)
    out = bytearray(orig)
    applied = skipped_long = 0
    for panel, recs in enumerate(panels):
        for slot, rec in enumerate(recs):
            eid = _invspell_id(panel, slot)
            zh = _translated(tr.get(eid), rec["name"], eid)
            if zh is None:
                continue
            encoded = encode_string(zh, char_to_id)
            if len(encoded) > INVSPELL_NAME_SIZE - 1:
                print(f"warning: {eid} translation {zh!r} encodes to {len(encoded)} bytes, "
                      f"exceeds the {INVSPELL_NAME_SIZE - 1}-byte field; keeping English",
                      file=sys.stderr)
                skipped_long += 1
                continue
            off = rec["rec_off"]
            out[off:off + INVSPELL_NAME_SIZE] = encoded + b"\0" * (INVSPELL_NAME_SIZE - len(encoded))
            applied += 1
    if skipped_long:
        print(f"  INVSPELL.DAT: {skipped_long} over-long name(s) left in English")
    return bytes(out), applied


def _verify_spells(orig: bytes, built: bytes) -> None:
    c0, n0 = decode_spells_dat(orig)
    c1, n1 = decode_spells_dat(built)
    if c0 != c1:
        raise AssertionError(f"SPELLS.DAT spell count changed {c0} -> {c1}")


def _verify_spelldoc(orig: bytes, built: bytes) -> None:
    r0, _ = decode_spelldoc_dat(orig)
    r1, _ = decode_spelldoc_dat(built)
    if r0 != r1:
        raise AssertionError(f"SPELLDOC.DAT row count changed {r0} -> {r1}")


def _verify_invspell(orig: bytes, built: bytes) -> None:
    if len(orig) != len(built):
        raise AssertionError(
            f"INVSPELL.DAT length changed {len(orig)} -> {len(built)} (must be patched in place)"
        )
    decode_invspell_dat(built)


def cmd_build(args: argparse.Namespace) -> None:
    tr = {
        e["id"]: e
        for e in json.loads(Path(args.json_path).read_text(encoding="utf-8")).get("entries", [])
    }
    char_to_id = json.loads(Path(args.mapping).read_text(encoding="utf-8"))["char_to_id"]
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    jobs = [
        ("SPELLS.DAT", args.spells, _build_spells, _verify_spells),
        ("SPELLDOC.DAT", args.spelldoc, _build_spelldoc, _verify_spelldoc),
        ("INVSPELL.DAT", args.invspell, _build_invspell, _verify_invspell),
    ]
    results: list[tuple[str, bytes, int]] = []
    for fname, src_path, build_fn, verify_fn in jobs:
        orig = Path(src_path).read_bytes()
        built, applied = build_fn(orig, tr, char_to_id)
        if len(built) >= MAX_FILE_SIZE:
            raise SystemExit(
                f"error: rebuilt {fname} is {len(built)} bytes (>= {MAX_FILE_SIZE:#x}); the "
                "engine's 16-bit blob-length cast would go negative -- shorten some translations"
            )
        verify_fn(orig, built)
        # an all-untranslated build must reproduce the input exactly
        if applied == 0 and built != orig:
            raise AssertionError(
                f"{fname}: no translations applied but the rebuild differs from the input "
                "(round-trip guarantee broken)"
            )
        results.append((fname, built, applied))

    for fname, built, applied in results:
        (out_dir / fname).write_bytes(built)
        print(f"Built {out_dir / fname}: {applied} translated")


# --------------------------------------------------------------------------- #
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Betrayal at Krondor spell-text translation pipeline "
                    "(SPELLS.DAT / SPELLDOC.DAT / INVSPELL.DAT)."
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("scaffold", help="Create/update the translation file from local originals.")
    p.add_argument("spells", help="Path to the local original SPELLS.DAT.")
    p.add_argument("spelldoc", help="Path to the local original SPELLDOC.DAT.")
    p.add_argument("invspell", help="Path to the local original INVSPELL.DAT.")
    p.add_argument("--out", help=f"Output JSON path (default: {_DEFAULT_JSON}).")
    p.set_defaults(func=cmd_scaffold)

    p = sub.add_parser("status", help="Show translation progress.")
    p.add_argument("json_path")
    p.add_argument("--show-untranslated", action="store_true")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("build", help="Merge translations into localized DAT files.")
    p.add_argument("spells", help="Path to the local original SPELLS.DAT.")
    p.add_argument("spelldoc", help="Path to the local original SPELLDOC.DAT.")
    p.add_argument("invspell", help="Path to the local original INVSPELL.DAT.")
    p.add_argument("json_path", help="Path to the translation JSON file.")
    p.add_argument("out_dir", help="Directory to write the three localized DAT files into.")
    p.add_argument("--mapping", default=str(_DEFAULT_MAPPING), help="Path to zh_mapping.json.")
    p.set_defaults(func=cmd_build)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
