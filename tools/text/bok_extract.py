#!/usr/bin/env python3
"""
Betrayal at Krondor -- BOK Book Extractor (Phase 7)

Parses a chapter-intro book file (`Cxx.BOK`, stored inside `krondor.001`)
into structured UTF-8 JSON. The engine side is `SRC/SCREENS/BOOKVIEW.C`
(`bookview_load_page_directory`) and `SRC/SCREENS/BOOKTEXT.C`.

On-disk layout
--------------
    u32  fileSize                 -- byte count of everything that follows
    --- everything below is the "directory blob", offsets are blob-relative ---
    i16  nPages
    u32  pageOffset[nPages]       -- blob-relative offset of each BookPage
    BookPage[0] .. BookPage[n-1]  -- stored back to back, in directory order

    BookPage (56 bytes):
        i16 x, y, w, h                 -- Rect
        u16 wDisplayNumber            -- printed page number (roman)
        u16 wPageNumber               -- logical id (nav fields reference this)
        u16 wPrevPageNumber
        u16 wNextPageNumber
        u16 wPagePointer             -- logical id that overflow text spills into
        u16 w_pad12                  -- non-zero => keep flowing into wPagePointer
        u16 wImageCount
        u16 wReservedCount           -- text-exclusion ("flow around") rectangles
        u16 wShowPageNumber
        u8  pReserved[30]            -- zero on disk; runtime resume state

    then wReservedCount * AbsRect(i16 x0,y0,x1,y1)   -- 8 bytes each
    then wImageCount   * BookImage(i16 x, i16 y, u16 imageIndex, u16 mirror)
    then the text stream, control-tagged, terminated by 0xF0:
        0xF1 + 16 bytes  -- layout block  (margins / line height / indent / align)
        0xF4 + 10 bytes  -- style block   (font slot / baseline / fg / bg / flags)
        0xF3 +  2 bytes  -- reserved word-hook (no-op in the shipped engine)
        0xF0             -- end of stream
        anything else    -- literal text byte

In every shipped book exactly one page (the first) carries the whole text
stream; the remaining pages are empty overflow targets the engine fills in
at render time.
"""

from __future__ import annotations

import argparse
import json
import struct
import sys
from pathlib import Path
from typing import Any

_PAGE_HDR = struct.Struct("<hhhh9H")  # Rect + 9 * u16   == 26 bytes
assert _PAGE_HDR.size == 26
_PAGE_HDR_TOTAL = 56  # + pReserved[30]

_CTRL_LEN = {0xF1: 17, 0xF4: 11, 0xF3: 3, 0xF0: 1}
_CTRL_KIND = {0xF1: "layout", 0xF4: "style", 0xF3: "hook", 0xF0: "end"}


def _parse_stream(blob: bytes, pos: int) -> tuple[list[dict[str, Any]], int]:
    """Parse a control-tagged text stream starting at `pos`; stop after 0xF0."""
    items: list[dict[str, Any]] = []
    run_index = 0
    text = bytearray()

    def flush() -> None:
        nonlocal text, run_index
        if text:
            items.append({
                "kind": "text",
                "run_index": run_index,
                "text": text.decode("latin1"),
            })
            run_index += 1
            text = bytearray()

    while pos < len(blob):
        byte = blob[pos]
        if byte in _CTRL_LEN:
            flush()
            length = _CTRL_LEN[byte]
            if pos + length > len(blob):
                raise ValueError(f"control block {byte:#x} at {pos:#x} truncated")
            item: dict[str, Any] = {"kind": _CTRL_KIND[byte]}
            if length > 1:
                item["hex"] = blob[pos + 1 : pos + length].hex()
            items.append(item)
            pos += length
            if byte == 0xF0:
                return items, pos
        elif (byte & 0xF0) == 0xF0:
            raise ValueError(f"unknown control byte {byte:#x} at {pos:#x}")
        else:
            text.append(byte)
            pos += 1

    raise ValueError("text stream is not 0xF0-terminated")


def extract_bok_data(payload: bytes) -> dict[str, Any]:
    if len(payload) < 6:
        raise ValueError("BOK payload too small")
    (file_size,) = struct.unpack_from("<I", payload, 0)
    blob = payload[4:]
    if file_size != len(blob):
        raise ValueError(
            f"BOK header size field {file_size} != trailing bytes {len(blob)}"
        )

    (page_count,) = struct.unpack_from("<h", blob, 0)
    if page_count < 1:
        raise ValueError(f"BOK page count {page_count} < 1")
    table_end = 2 + page_count * 4
    if table_end > len(blob):
        raise ValueError("BOK page-offset table truncated")
    page_offsets = [
        struct.unpack_from("<I", blob, 2 + i * 4)[0] for i in range(page_count)
    ]

    pages: list[dict[str, Any]] = []
    for i, off in enumerate(page_offsets):
        if off + _PAGE_HDR_TOTAL > len(blob):
            raise ValueError(f"page {i} header at {off:#x} out of bounds")
        x, y, w, h, disp, num, prev, nxt, ptr, pad12, n_img, n_rsvd, show = (
            _PAGE_HDR.unpack_from(blob, off)
        )
        p = off + _PAGE_HDR.size
        reserved_hex = blob[p : p + 30].hex()
        p += 30

        reserved_rects = []
        for _ in range(n_rsvd):
            reserved_rects.append(list(struct.unpack_from("<hhhh", blob, p)))
            p += 8

        images = []
        for _ in range(n_img):
            ix, iy, idx, mir = struct.unpack_from("<hhHH", blob, p)
            images.append([ix, iy, idx, mir])
            p += 8

        stream, _ = _parse_stream(blob, p)

        pages.append({
            "index": i,
            "rect": [x, y, w, h],
            "wDisplayNumber": disp,
            "wPageNumber": num,
            "wPrevPageNumber": prev,
            "wNextPageNumber": nxt,
            "wPagePointer": ptr,
            "w_pad12": pad12,
            "wImageCount": n_img,
            "wReservedCount": n_rsvd,
            "wShowPageNumber": show,
            "pReserved_hex": reserved_hex,
            "reserved_rects": reserved_rects,
            "images": images,
            "stream": stream,
        })

    return {
        "format": "BAK_BOK",
        "version": 1,
        "page_count": page_count,
        "pages": pages,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract a Betrayal at Krondor .BOK book to JSON.")
    parser.add_argument("input_bok", type=Path, help="Path to input .BOK file")
    parser.add_argument("output_json", type=Path, nargs="?", help="Output .json path (optional)")
    args = parser.parse_args()

    extracted = extract_bok_data(args.input_bok.read_bytes())
    out_path = args.output_json or args.input_bok.with_suffix(".json")
    out_path.write_text(json.dumps(extracted, indent=2, ensure_ascii=False), encoding="utf-8")

    runs = sum(1 for pg in extracted["pages"] for it in pg["stream"] if it["kind"] == "text")
    print(f"Extracted {extracted['page_count']} page(s), {runs} text run(s) to {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
