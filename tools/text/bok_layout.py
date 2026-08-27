#!/usr/bin/env python3
"""
Betrayal at Krondor -- BOK layout adjustments for Chinese text.

Two in-place transforms on the structured dict from ``bok_extract``, applied
by the zh build (``bok_rebuild_common``) between parsing the pristine book and
repacking it. Both are pure ``.BOK`` data -- no engine change.

1. ``raise_line_height`` -- every ``0xF1`` layout block ships ``nLineHeight``
   = 15, which is fine for the ~11px-tall BOOK.FNT English glyphs but 1px
   SHORTER than a 16px Chinese glyph, so translated lines touch/overlap.
   Bump it to a readable pitch.

2. ``append_overflow_pages`` -- BOK page counts are fixed in the file and the
   engine truncates any text that overruns the last page. Taller lines can
   push a dense book's text past its last page, so append blank overflow
   pages and re-chain navigation. Non-tail pages keep
   ``wNextPageNumber == wPagePointer``; the engine's terminate check
   (BOOKVIEW.C: ``wNextPageNumber == wPagePointer && nTerminate``) then stops
   the book on whichever page the text actually ends, so unused spare pages
   are never shown -- the reader only sees a spare if the text really needs it.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bok_extract import _PAGE_HDR_TOTAL  # noqa: E402

_TERMINATORS = (0xFFFE, 0xFFFF)
DEFAULT_LINE_HEIGHT = 18
# Appending pages to a .BOK corrupted the world-renderer palette state in
# testing (garbage stripes on the travel map). Kept for investigation; not
# used by the build.
DEFAULT_SPARE_PAGES = 0


def raise_line_height(extracted: dict[str, Any], target: int = DEFAULT_LINE_HEIGHT) -> int:
    """Raise nLineHeight (3rd i16 of each 0xF1 layout block) to at least `target`.

    Returns the number of layout blocks changed.
    """
    changed = 0
    for page in extracted["pages"]:
        for item in page["stream"]:
            if item.get("kind") != "layout":
                continue
            payload = bytearray.fromhex(item["hex"])  # 16 bytes = 8 * i16
            line_height = int.from_bytes(payload[4:6], "little", signed=True)
            if line_height < target:
                payload[4:6] = int(target).to_bytes(2, "little", signed=True)
                item["hex"] = payload.hex()
                changed += 1
    return changed


def _blank_page(index: int, num: int, prev_num: int, next_num: int, ptr: int,
                disp: int, show: int, rect: list[int]) -> dict[str, Any]:
    return {
        "index": index,
        "rect": list(rect),
        "wDisplayNumber": disp,
        "wPageNumber": num,
        "wPrevPageNumber": prev_num,
        "wNextPageNumber": next_num,
        "wPagePointer": ptr,
        "w_pad12": 0,
        "wImageCount": 0,
        "wReservedCount": 0,
        "wShowPageNumber": show,
        "pReserved_hex": "00" * 30,
        "reserved_rects": [],
        "images": [],
        "stream": [{"kind": "end"}],
    }


def append_overflow_pages(extracted: dict[str, Any], count: int = DEFAULT_SPARE_PAGES) -> int:
    """Append `count` blank overflow pages after the book's tail page.

    Returns the number of pages added (0 if the book's tail is non-standard,
    e.g. C94, which is left untouched).
    """
    if count <= 0:
        return 0
    pages = extracted["pages"]
    nums = {p["wPageNumber"] for p in pages}

    tail = next((p for p in pages if p["wNextPageNumber"] not in nums), None)
    if tail is None or tail["wNextPageNumber"] not in _TERMINATORS:
        # No clean tail (or a hand-authored non-standard chain) -- don't touch.
        return 0

    orig_next, orig_ptr = tail["wNextPageNumber"], tail["wPagePointer"]
    first_spare = max(nums) + 1
    tail["wNextPageNumber"] = first_spare
    tail["wPagePointer"] = first_spare

    prev_num = tail["wPageNumber"]
    for i in range(count):
        num = first_spare + i
        is_last = i == count - 1
        pages.append(_blank_page(
            index=len(pages),
            num=num,
            prev_num=prev_num,
            next_num=orig_next if is_last else num + 1,
            ptr=orig_ptr if is_last else num + 1,
            disp=tail["wDisplayNumber"] + 1 + i,
            show=tail["wShowPageNumber"],
            rect=tail["rect"],
        ))
        prev_num = num

    extracted["page_count"] = len(pages)
    return count


def adjust_for_chinese(extracted: dict[str, Any],
                       line_height: int = DEFAULT_LINE_HEIGHT,
                       spare_pages: int = DEFAULT_SPARE_PAGES) -> dict[str, int]:
    """Apply both transforms; returns a small stats dict."""
    return {
        "layout_blocks_retuned": raise_line_height(extracted, line_height),
        "spare_pages_added": append_overflow_pages(extracted, spare_pages),
    }


assert _PAGE_HDR_TOTAL == 56  # blank page relies on the 56-byte header layout
