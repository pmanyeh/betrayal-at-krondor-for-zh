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

try:
    from .build_font import build_small_zh_font
except ImportError:
    from build_font import build_small_zh_font


def chars_from_translations(paths: list[Path]) -> list[str]:
    """Collects glyphs from every given translation source. A small-font glyph
    table is sparse and used by more than one UI surface at once (e.g. the
    character sheet's stat panel AND the chapter-title banner both use the
    10x10 small font) -- passing only one source silently drops any glyph the
    OTHER surface needs, even though both surfaces render fine individually.
    Always pass every source that shares this font, not just the one you're
    currently working on."""
    chars: dict[str, None] = {}
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        for entry in data.get("entries", []):
            if entry.get("status") != "translated":
                continue
            for ch in entry.get("translation", ""):
                if ord(ch) >= 0x2E80:
                    chars.setdefault(ch, None)
        for entry in data.get("injected_entries", []):
            for field in ("label", "primary", "alt"):
                for ch in entry.get(field, "") or "":
                    if ord(ch) >= 0x2E80:
                        chars.setdefault(ch, None)
    return list(chars)


def chars_from_ddx_small_text(translated_dir: Path) -> list[str]:
    """Collect translated DDX text that is rendered with the small font.

    This includes ``#title#`` prefixes rendered by dialog_draw_speech_bubble()
    and complete records whose translation notes explicitly identify the
    chapter-banner 10x10 path.  Keeping the selection structural/explicit
    avoids putting every character in every DDX body into ZHSTAT, whose DOS
    renderer performs a linear glyph lookup.
    """
    chars: dict[str, None] = {}
    for path in sorted(translated_dir.glob("DIAL_*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for entry in data.get("entries", []):
            if entry.get("status") != "translated":
                continue
            text = entry.get("translation", "")
            if "10x10 Chinese font path" in entry.get("notes", ""):
                for ch in text:
                    if ord(ch) >= 0x2E80:
                        chars.setdefault(ch, None)
            if not text.startswith("#"):
                continue
            end = text.find("#", 1)
            if end < 0:
                continue
            for ch in text[1:end]:
                if ord(ch) >= 0x2E80:
                    chars.setdefault(ch, None)
    return list(chars)


def chars_from_ddx_titles(translated_dir: Path) -> list[str]:
    """Backward-compatible name for callers written before marked panels."""
    return chars_from_ddx_small_text(translated_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a sparse small-cell ZHSM font.")
    parser.add_argument("translations", type=Path, nargs="+",
                         help="One or more localization/translated/*.json sources -- "
                              "pass every source that shares this small font, not just one.")
    parser.add_argument("--zh-mapping", type=Path, required=True,
                         help="localization/generated/zh_mapping.json (for glyph IDs)")
    parser.add_argument("--cell", type=int, default=10, help="Glyph cell size in pixels")
    parser.add_argument(
        "--ddx-title-dir",
        type=Path,
        help="Also include translated #title# prefixes and marked 10x10 DDX panels",
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    char_to_id = json.loads(args.zh_mapping.read_text(encoding="utf-8"))["char_to_id"]
    chars = chars_from_translations(args.translations)
    if args.ddx_title_dir is not None:
        chars = list(dict.fromkeys(chars + chars_from_ddx_small_text(args.ddx_title_dir)))
    blob = build_small_zh_font(chars, char_to_id, cell=args.cell)
    args.output.write_bytes(blob)
    print(f"Built {len(chars)} small glyph(s) ({args.cell}x{args.cell}) -> {args.output} ({len(blob)} bytes)")


if __name__ == "__main__":
    main()
