#!/usr/bin/env python3
"""
Betrayal at Krondor -- MenuPage (.dat) button-label translation.

The req_*.dat / contents.dat files inside KRONDOR.RMF are the game's menu
resources (main menu, save/load, Options, camp, map, inventory, guild, knock,
teleport ...). menupage_load() (SRC/UI/MENUPAGE.C) reads them:

    28 bytes  MenuPage header  -- only u16 pTitle at file offset 18 matters
                                  (blob offset of the title string, or 0xFFFF)
    u16       entry count
    count * 33 bytes  MenuEntry -- u16 pLabel @+19, u16 pPrimary_label @+21,
                                   u16 pAlt_label @+23 (each a blob offset or
                                   0xFFFF = none)
    u16       blob size
    blob      NUL-terminated string pool (offsets are blob-relative)

Labels render through widget_dispatch_by_type -> uiwidget_draw_text_shadowed ->
font_draw_text_far, which already handles the BAK-ZH double-byte encoding.
(The 15px button height is too short for 16px glyphs -- WIDGET.C draws menu
button labels with g_bSmallZhMode so they render at 10x10.)

Rebuilt append-only: the original blob is kept byte-for-byte and translated
slots are repointed at freshly appended strings; blob size is rewritten. An
all-untranslated build reproduces the input exactly (asserted by `build`).

One JSON covers every file. Entry id = "<FILE>#<n>#<slot>" where slot is
title | label | primary | alt and n is the entry index (0 for the title).

    scaffold <pristine-dir> [--out ...]
    status   <json>
    build    <pristine-dir> <json> <out-dir> [--mapping ...]
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
    Path(__file__).resolve().parents[2] / "localization" / "translated" / "MENUPAGE.json"
)

HEADER_SIZE = 28
TITLE_OFF = 18
ENTRY_SIZE = 0x21
SLOT_OFFSETS = {"label": 19, "primary": 21, "alt": 23}
NONE = 0xFFFF


def _resolve(blob: bytes, off: int) -> str | None:
    if off == NONE:
        return None
    end = blob.find(b"\0", off)
    if end < 0:
        raise ValueError(f"string at blob offset {off:#x} is not NUL terminated")
    return blob[off:end].decode("latin1")


def decode_menupage(payload: bytes) -> dict[str, Any]:
    if len(payload) < HEADER_SIZE + 2:
        raise ValueError("menupage file is shorter than its header")
    (title_off,) = struct.unpack_from("<H", payload, TITLE_OFF)
    (count,) = struct.unpack_from("<H", payload, HEADER_SIZE)
    entries_start = HEADER_SIZE + 2
    blob_off = entries_start + count * ENTRY_SIZE
    if blob_off + 2 > len(payload):
        raise ValueError(f"menupage entry table for {count} entries is truncated")
    (blob_size,) = struct.unpack_from("<H", payload, blob_off)
    blob = payload[blob_off + 2: blob_off + 2 + blob_size]
    if len(blob) != blob_size:
        raise ValueError(
            f"menupage blob is {len(blob)} bytes, header declares {blob_size}"
        )

    out: dict[str, Any] = {"count": count, "title": _resolve(blob, title_off), "entries": []}
    for i in range(count):
        base = entries_start + i * ENTRY_SIZE
        slots = {}
        for slot, rel in SLOT_OFFSETS.items():
            (off,) = struct.unpack_from("<H", payload, base + rel)
            slots[slot] = _resolve(blob, off)
        out["entries"].append(slots)
    return out


def _menu_files(pristine_dir: Path) -> list[Path]:
    return sorted(
        p for p in pristine_dir.iterdir()
        if p.suffix.lower() == ".dat" and (p.name.lower().startswith("req_")
                                           or p.name.lower() == "contents.dat")
    )


def _entry_id(fname: str, n: int, slot: str) -> str:
    return f"{fname}#{n}#{slot}"


def cmd_scaffold(args: argparse.Namespace) -> None:
    pristine = Path(args.pristine_dir)
    files = _menu_files(pristine)
    if not files:
        raise SystemExit(f"error: no req_*.dat / contents.dat found in {pristine}")

    out_path = Path(args.out) if args.out else _DEFAULT_JSON
    existing: dict[str, dict[str, Any]] = {}
    existing_data: dict[str, Any] = {}
    if out_path.exists():
        existing_data = json.loads(out_path.read_text(encoding="utf-8"))
        for e in existing_data.get("entries", []):
            existing[e["id"]] = e

    entries: list[dict[str, Any]] = []
    drifted: list[str] = []
    files_with_text = 0
    for path in files:
        page = decode_menupage(path.read_bytes())
        fname = path.name.upper()
        rows: list[tuple[int, str, str]] = []
        if page["title"] is not None:
            rows.append((0, "title", page["title"]))
        for i, slots in enumerate(page["entries"]):
            for slot in ("label", "primary", "alt"):
                if slots[slot]:
                    rows.append((i, slot, slots[slot]))
        if rows:
            files_with_text += 1
        for n, slot, src in rows:
            eid = _entry_id(fname, n, slot)
            prior = existing.get(eid)
            if prior is not None and prior.get("source") != src:
                drifted.append(eid)
            entries.append({
                "id": eid,
                "file": fname,
                "entry": n,
                "slot": slot,
                "source": src,
                "translation": prior["translation"] if prior else "",
                "status": prior["status"] if prior else "untranslated",
                "notes": prior["notes"] if prior else "",
            })

    if drifted:
        print(f"warning: {len(drifted)} id(s) drifted: {drifted[:10]}"
              f"{' ...' if len(drifted) > 10 else ''}", file=sys.stderr)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    result = {
        "format": "BAK_ZH_MENUPAGE_TRANSLATION",
        "version": 1,
        "source_files": [p.name.upper() for p in files],
        "entries": entries,
    }
    if existing_data.get("injected_entries"):
        result["injected_entries"] = existing_data["injected_entries"]
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    uniq = len({e["source"] for e in entries})
    translated = sum(1 for e in entries if e["status"] == "translated")
    print(f"Scaffolded {len(entries)} label(s) ({uniq} distinct) from {files_with_text}/"
          f"{len(files)} files with text, {translated} already translated -> {out_path}")


def cmd_status(args: argparse.Namespace) -> None:
    data = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    by_status: dict[str, int] = {}
    for e in entries:
        by_status[e["status"]] = by_status.get(e["status"], 0) + 1
    print(f"{data.get('format', '?')}: {len(entries)} labels "
          f"({len({e['source'] for e in entries})} distinct)")
    for status, count in sorted(by_status.items()):
        print(f"  {status}: {count}")
    if args.show_untranslated:
        seen = set()
        for e in entries:
            if e["status"] == "untranslated" and e["source"] not in seen:
                seen.add(e["source"])
                print(f"  {e['source']!r}")


def _build_one(orig: bytes, rows: dict[tuple[int, str], str], char_to_id: dict) -> tuple[bytes, int, int]:
    """rows maps (entry_index, slot) -> translated string. slot 'title' uses
    entry_index 0. Returns (bytes, applied, skipped_too_long).

    The whole string pool is rebuilt, not appended to. menupage_free()
    recovers the malloc base of the string blob by taking the *minimum* of
    every non-NULL label pointer, so the pool must be laid out with a
    referenced string at offset 0 -- an append-only rebuild orphans the
    original offset-0 string and makes menupage_free() my_free() an interior
    pointer, corrupting the heap (MEM:34). Emitting the pool in
    title-then-entry reference order keeps a live string at offset 0.
    """
    (count,) = struct.unpack_from("<H", orig, HEADER_SIZE)
    entries_start = HEADER_SIZE + 2
    blob_off = entries_start + count * ENTRY_SIZE

    if not rows:
        return orig, 0, 0  # byte-identical fast path

    (title_off,) = struct.unpack_from("<H", orig, TITLE_OFF)
    orig_blob = orig[blob_off + 2:]

    def local(n: int, slot: str) -> str | None:
        off = title_off if slot == "title" else \
            struct.unpack_from("<H", orig, entries_start + n * ENTRY_SIZE + SLOT_OFFSETS[slot])[0]
        return _resolve(orig_blob, off)

    # every slot in the file, in the order menupage_free scans them, with the
    # translation substituted where we have one.
    slots: list[tuple[int, str]] = [(0, "title")]
    for i in range(count):
        slots += [(i, "label"), (i, "primary"), (i, "alt")]

    pool = bytearray()
    interned: dict[bytes, int] = {}
    new_off: dict[tuple[int, str], int] = {}
    applied = skipped_long = 0
    for key in slots:
        src = local(*key)
        if src is None:
            continue
        zh = rows.get(key)
        if zh is not None:
            data = encode_string(zh, char_to_id)
            if len(data) > 200:  # sanity guard; menu labels are tiny
                print(f"warning: menupage label {zh!r} encodes to {len(data)} bytes; "
                      f"keeping English", file=sys.stderr)
                skipped_long += 1
                data = src.encode("latin1")
            else:
                applied += 1
        else:
            data = src.encode("latin1")
        data += b"\0"
        if data not in interned:
            if len(pool) + len(data) > 0xFFFF:
                raise ValueError("menupage string pool exceeds a 16-bit offset")
            interned[data] = len(pool)
            pool.extend(data)
        new_off[key] = interned[data]

    out = bytearray(orig[:blob_off])
    struct.pack_into("<H", out, TITLE_OFF,
                     new_off.get((0, "title"), title_off) if title_off != NONE else NONE)
    for i in range(count):
        base = entries_start + i * ENTRY_SIZE
        for slot, rel in SLOT_OFFSETS.items():
            cur = struct.unpack_from("<H", orig, base + rel)[0]
            struct.pack_into("<H", out, base + rel,
                             new_off.get((i, slot), cur) if cur != NONE else NONE)
    out.extend(struct.pack("<H", len(pool)))
    out.extend(pool)
    return bytes(out), applied, skipped_long


def _inject_entries(payload: bytes, specs: list[dict[str, Any]], char_to_id: dict) -> bytes:
    """Insert explicitly declared buttons after the normal translated rebuild.

    Each injected entry clones an existing record for its widget styling, then
    replaces its action, rectangle, and label pointers. Existing blob offsets
    remain valid because the string pool stays in place and the new strings are
    appended; unlike translation-by-append, this cannot orphan blob offset 0.
    """
    if not specs:
        return payload

    (count,) = struct.unpack_from("<H", payload, HEADER_SIZE)
    entries_start = HEADER_SIZE + 2
    blob_off = entries_start + count * ENTRY_SIZE
    (blob_size,) = struct.unpack_from("<H", payload, blob_off)
    records = [bytearray(payload[entries_start + i * ENTRY_SIZE:
                                 entries_start + (i + 1) * ENTRY_SIZE])
               for i in range(count)]
    blob = bytearray(payload[blob_off + 2:blob_off + 2 + blob_size])

    for spec in specs:
        insert_at = int(spec["insert_at"])
        copy_entry = int(spec["copy_entry"])
        if not 0 <= insert_at <= len(records):
            raise ValueError(f"injected entry insert_at {insert_at} is out of range")
        if not 0 <= copy_entry < len(records):
            raise ValueError(f"injected entry copy_entry {copy_entry} is out of range")
        rec = bytearray(records[copy_entry])
        struct.pack_into("<H", rec, 2, int(spec["action_id"]))
        rect = spec["rect"]
        if len(rect) != 4:
            raise ValueError("injected entry rect must be [x, y, width, height]")
        struct.pack_into("<hhhh", rec, 11, *(int(v) for v in rect))

        for slot, rel in SLOT_OFFSETS.items():
            text = spec.get(slot)
            if text is None:
                struct.pack_into("<H", rec, rel, NONE)
                continue
            encoded = encode_string(text, char_to_id) + b"\0"
            if len(blob) + len(encoded) > 0xFFFF:
                raise ValueError("menupage string pool exceeds a 16-bit offset")
            struct.pack_into("<H", rec, rel, len(blob))
            blob.extend(encoded)
        records.insert(insert_at, rec)

    out = bytearray(payload[:HEADER_SIZE])
    out.extend(struct.pack("<H", len(records)))
    for rec in records:
        out.extend(rec)
    out.extend(struct.pack("<H", len(blob)))
    out.extend(blob)
    return bytes(out)


def cmd_build(args: argparse.Namespace) -> None:
    pristine = Path(args.pristine_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    char_to_id = json.loads(Path(args.mapping).read_text(encoding="utf-8"))["char_to_id"]

    catalog = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
    tr = catalog.get("entries", [])
    injections_by_file: dict[str, list[dict[str, Any]]] = {}
    for spec in catalog.get("injected_entries", []):
        injections_by_file.setdefault(spec["file"], []).append(spec)
    by_file: dict[str, dict[tuple[int, str], str]] = {}
    by_file_src: dict[str, dict[tuple[int, str], str]] = {}
    for e in tr:
        if e["status"] != "translated" or not e["translation"]:
            continue
        by_file.setdefault(e["file"], {})[(e["entry"], e["slot"])] = e["translation"]
        by_file_src.setdefault(e["file"], {})[(e["entry"], e["slot"])] = e["source"]

    total_applied = total_long = total_drift = 0
    built_files = 0
    for path in _menu_files(pristine):
        fname = path.name.upper()
        orig = path.read_bytes()
        page = decode_menupage(orig)
        rows = dict(by_file.get(fname, {}))

        # drop drifted slots (source in json no longer matches the file)
        for key in list(rows):
            n, slot = key
            local = page["title"] if slot == "title" else page["entries"][n][slot]
            if local != by_file_src.get(fname, {}).get(key):
                print(f"warning: {_entry_id(fname, n, slot)} source drift; keeping the local "
                      f"string", file=sys.stderr)
                del rows[key]
                total_drift += 1

        built, applied, skipped_long = _build_one(orig, rows, char_to_id)
        built = _inject_entries(built, injections_by_file.get(fname, []), char_to_id)
        # validate + round-trip guarantee
        decode_menupage(built)
        if applied == 0 and not injections_by_file.get(fname) and built != orig:
            raise AssertionError(f"{fname}: no translations applied but rebuild differs from input")
        (out_dir / path.name).write_bytes(built)
        total_applied += applied
        total_long += skipped_long
        if applied:
            built_files += 1

    print(f"Built {built_files} localized file(s) into {out_dir}: {total_applied} label(s) "
          f"translated, {total_long} too-long fallback(s), {total_drift} source-drift fallback(s)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Betrayal at Krondor MenuPage (.dat) button-label translation pipeline."
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("scaffold", help="Create/update the translation file from a pristine dir.")
    p.add_argument("pristine_dir", help="Directory of original req_*.dat / contents.dat files.")
    p.add_argument("--out", help=f"Output JSON path (default: {_DEFAULT_JSON}).")
    p.set_defaults(func=cmd_scaffold)

    p = sub.add_parser("status", help="Show translation progress.")
    p.add_argument("json_path")
    p.add_argument("--show-untranslated", action="store_true")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("build", help="Merge translations into localized .dat files.")
    p.add_argument("pristine_dir", help="Directory of original req_*.dat / contents.dat files.")
    p.add_argument("json_path", help="Path to the translation JSON file.")
    p.add_argument("out_dir", help="Directory to write the localized .dat files into.")
    p.add_argument("--mapping", default=str(_DEFAULT_MAPPING), help="Path to zh_mapping.json.")
    p.set_defaults(func=cmd_build)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
