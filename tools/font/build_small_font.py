#!/usr/bin/env python3
"""
Betrayal at Krondor — Small-Cell Chinese Font Builder

Builds a sparse ZHSM-format small glyph table (see build_zh_font in build_font.py)
covering only the characters used by a given translation source, keyed by the
main ZH16 font's glyph IDs. Used for UI surfaces that need a smaller CJK glyph
than the game's standard 16x16 (e.g. the character sheet's cramped "Ratings:"
stat box, originally designed for an ~11px-tall English font).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_font import build_small_zh_font


def chars_from_translations(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    chars: dict[str, None] = {}
    for entry in data.get("entries", []):
        if entry.get("status") != "translated":
            continue
        for ch in entry.get("translation", ""):
            if ord(ch) >= 0x2E80:
                chars.setdefault(ch, None)
    return list(chars)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a sparse small-cell ZHSM font.")
    parser.add_argument("translations", type=Path, help="localization/translated/*.json source")
    parser.add_argument("--zh-mapping", type=Path, required=True,
                         help="localization/generated/zh_mapping.json (for glyph IDs)")
    parser.add_argument("--cell", type=int, default=10, help="Glyph cell size in pixels")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    char_to_id = json.loads(args.zh_mapping.read_text(encoding="utf-8"))["char_to_id"]
    chars = chars_from_translations(args.translations)
    blob = build_small_zh_font(chars, char_to_id, cell=args.cell)
    args.output.write_bytes(blob)
    print(f"Built {len(chars)} small glyph(s) ({args.cell}x{args.cell}) -> {args.output} ({len(blob)} bytes)")


if __name__ == "__main__":
    main()
