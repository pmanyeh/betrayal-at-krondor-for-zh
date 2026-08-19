#!/usr/bin/env python3
"""
Betrayal at Krondor — Chinese Font & Encoding Tool (Phase 3)
Builds ZH16.DAT font binary and provides BAK-ZH Compact 2-Byte Encoding / Decoding.
"""

from __future__ import annotations

import argparse
import json
import struct
from pathlib import Path
from typing import Any

# BAK-ZH Compact Encoding Constants
LEAD_MIN = 0x80
LEAD_MAX = 0xDF  # 96 leads
TRAIL_PART1_MIN = 0x20
TRAIL_PART1_MAX = 0x7E  # 95 values
TRAIL_PART2_MIN = 0x80
TRAIL_PART2_MAX = 0xDF  # 96 values (we use 65 values: 0x80..0xC0)
SLOTS_PER_LEAD = 160  # 95 + 65 = 160 glyphs per lead byte
MAX_GLYPHS = (LEAD_MAX - LEAD_MIN + 1) * SLOTS_PER_LEAD  # 96 * 160 = 15,360

# Default POC 50 Glyph List
POC_GLYPHS = (
    "歐文我們在哪裡克朗多洛爾戈拉斯塔"
    "主選單開始繼續設定離庫存裝備觀察"
    "金幣隊伍戰鬥攻擊防禦魔法逃跑投降"
    "道具說明是否"
    "猛然向前撲去鎖鏈他腕間如屬毒蛇般扭動"
    "特一躍手之的鐵鍊像著"
)


def glyph_id_to_bytes(glyph_id: int) -> bytes:
    """Encodes a Glyph ID (0..15359) into 2-byte BAK-ZH game encoding."""
    if not (0 <= glyph_id < MAX_GLYPHS):
        raise ValueError(f"Glyph ID {glyph_id} exceeds maximum capacity {MAX_GLYPHS}")

    lead_idx = glyph_id // SLOTS_PER_LEAD
    trail_idx = glyph_id % SLOTS_PER_LEAD

    lead = LEAD_MIN + lead_idx
    if trail_idx < 95:
        trail = TRAIL_PART1_MIN + trail_idx
    else:
        trail = TRAIL_PART2_MIN + (trail_idx - 95)

    return bytes([lead, trail])


def bytes_to_glyph_id(lead: int, trail: int) -> int:
    """Decodes 2-byte BAK-ZH game encoding into a Glyph ID."""
    if not (LEAD_MIN <= lead <= LEAD_MAX):
        raise ValueError(f"Invalid Lead byte {lead:#x}")

    lead_idx = lead - LEAD_MIN
    if TRAIL_PART1_MIN <= trail <= TRAIL_PART1_MAX:
        trail_idx = trail - TRAIL_PART1_MIN
    elif TRAIL_PART2_MIN <= trail <= TRAIL_PART2_MAX:
        trail_idx = 95 + (trail - TRAIL_PART2_MIN)
    else:
        raise ValueError(f"Invalid Trail byte {trail:#x}")

    return lead_idx * SLOTS_PER_LEAD + trail_idx


def encode_string(text: str, char_to_id: dict[str, int]) -> bytes:
    """Encodes a Unicode text string into BAK-ZH game encoded bytes."""
    output = bytearray()
    for ch in text:
        code = ord(ch)
        if code < 0x80:
            # Standard ASCII (0..127)
            output.append(code)
        elif ch in char_to_id:
            output.extend(glyph_id_to_bytes(char_to_id[ch]))
        elif 0xE0 <= code <= 0xFF:
            # Raw style/control byte (font_render_glyph_or_ctrl), carried
            # over verbatim from the source text -- never Chinese-encoded,
            # since 0xE0-0xFF is outside the 0x80-0xDF lead-byte range.
            output.append(code)
        else:
            # Fallback for unmapped characters: '?'
            output.append(ord("?"))
    return bytes(output)


def decode_string(data: bytes, id_to_char: dict[int, str]) -> str:
    """Decodes BAK-ZH game encoded bytes into a Unicode string."""
    out = []
    i = 0
    length = len(data)
    while i < length:
        b = data[i]
        if b < 0x80:
            out.append(chr(b))
            i += 1
        elif LEAD_MIN <= b <= LEAD_MAX:
            if i + 1 < length:
                trail = data[i + 1]
                try:
                    gid = bytes_to_glyph_id(b, trail)
                    out.append(id_to_char.get(gid, "?"))
                    i += 2
                    continue
                except ValueError:
                    pass
            out.append("?")
            i += 1
        else:
            # Control code or undefined high byte (0xE0..0xFF)
            out.append(f"\\x{b:02x}")
            i += 1
    return "".join(out)


# ETen 3.53 native bitmap font (STDFONT.15 hanzi + SPCFONT.15 punctuation,
# 16x15 1bpp, 30-byte stride). This is the actual period-authentic 1993 DOS
# Chinese font — index math and oracle verified against known glyphs (idx 0 is
# "一", A4A4 is "中", A143 is the "。" glyph in SPCFONT).
_ETEN_STD_PATH = r"D:\git\Fonts\iso\FILES\STDFONT.15"
_ETEN_SPC_PATH = r"D:\git\Fonts\iso\FILES\SPCFONT.15"
_ETEN_STRIDE = 30
_ETEN_N_COMMON = 5401  # count of the "common" hanzi block (A440-C67E)

_eten_banks: dict[str, bytes] = {}


def _eten_big5_raw(hi: int, lo: int) -> int:
    return (hi - 0xA1) * 157 + ((lo - 0x40) if lo < 0x7F else (lo - 0x62))


def _eten_glyph_slot(hi: int, lo: int) -> tuple[str, int] | None:
    r = _eten_big5_raw(hi, lo)
    last_spc = _eten_big5_raw(0xA3, 0xBF)
    base_a440 = _eten_big5_raw(0xA4, 0x40)
    last_common = _eten_big5_raw(0xC6, 0x7E)
    base_c940 = _eten_big5_raw(0xC9, 0x40)
    if r < 0:
        return None
    if r <= last_spc:
        return ("spc", r)
    if r < base_a440:
        return None
    if r <= last_common:
        return ("std", r - base_a440)
    if r < base_c940:
        return None
    return ("std", _ETEN_N_COMMON + (r - base_c940))


def render_glyph_from_eten(char: str) -> bytes | None:
    """Rasterizes a single character from the real ETen 3.53 16x15 bitmap font,
    padded to 16x16 (32 bytes) with a blank trailing row. Returns None if the
    font files aren't available or the character isn't representable in Big5."""
    for key, path in (("std", _ETEN_STD_PATH), ("spc", _ETEN_SPC_PATH)):
        if key not in _eten_banks:
            try:
                _eten_banks[key] = Path(path).read_bytes()
            except OSError:
                return None

    try:
        raw = char.encode("big5")
    except (UnicodeEncodeError, LookupError):
        return None
    if len(raw) != 2:
        return None
    slot = _eten_glyph_slot(raw[0], raw[1])
    if slot is None:
        return None
    bank_name, idx = slot
    bank = _eten_banks[bank_name]
    offset = idx * _ETEN_STRIDE
    if offset + _ETEN_STRIDE > len(bank):
        return None
    return bank[offset : offset + _ETEN_STRIDE] + b"\x00\x00"


# (path, size): size is the point size at which each font's CJK grid renders
# pixel-crisp (no antialiasing) — verified empirically per font, not a guess.
# Fusion Pixel is a genuine pixel-art font (authentic blocky retro look, matches
# the game's era); Microsoft JhengHei is a smooth outline font used as fallback.
_TTF_FONT_CANDIDATES = (
    (r"C:\Windows\Fonts\mingliu.ttc", 15),  # MingLiU / 新細明體
    (r"D:\git\Fonts\Fusion_Pixel_10px.ttf", 14),
    (r"C:\Windows\Fonts\msjh.ttc", 15),
)


def render_glyph_from_ttf(
    char: str, font_path: str | None = None, size: int | None = None
) -> bytes | None:
    """Rasterizes a single character to a 16x16 monochrome bitmap (32 bytes) using an
    installed TTF/TTC, tightly cropped to its ink and centered in the 16x16 cell.
    Returns None if Pillow or a usable font isn't available, so callers can fall
    back to generate_synthetic_glyph."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return None

    candidates = ((font_path, size or 15),) if font_path else _TTF_FONT_CANDIDATES
    font = None
    for path, pt_size in candidates:
        if path is None:
            continue
        try:
            font = ImageFont.truetype(path, pt_size)
            break
        except OSError:
            continue
    if font is None:
        return None

    big = Image.new("L", (32, 32), 0)
    draw = ImageDraw.Draw(big)
    draw.text((8, 8), char, font=font, fill=255)
    bbox = big.getbbox()
    canvas = Image.new("L", (16, 16), 0)
    if bbox is not None:
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        ox, oy = max(0, (16 - w) // 2), max(0, (16 - h) // 2)
        canvas.paste(big.crop(bbox), (ox, oy))
    px = canvas.load()

    rows = bytearray()
    for y in range(16):
        bits = 0
        for x in range(16):
            if px[x, y] > 128:
                bits |= 1 << (15 - x)
        rows.append((bits >> 8) & 0xFF)
        rows.append(bits & 0xFF)
    return bytes(rows)


def generate_synthetic_glyph(char: str, glyph_id: int) -> bytes:
    """Generates a high-contrast 16x16 monochrome bitmap (32 bytes) for testing."""
    # 16 rows, 2 bytes (16 bits) per row
    rows = [0] * 16

    # Draw border box
    rows[0] = 0xFFFE  # Top border
    rows[15] = 0xFFFE  # Bottom border
    for r in range(1, 15):
        rows[r] = 0x8002  # Left and right side borders

    # Draw a unique pattern based on glyph_id inside the box
    # Cross or diagonal lines so each glyph has distinct recognizable pixel pattern
    pattern_type = glyph_id % 4
    if pattern_type == 0:
        # Cross '+'
        rows[7] |= 0x1FF0
        rows[8] |= 0x1FF0
        for r in range(3, 13):
            rows[r] |= 0x0180
    elif pattern_type == 1:
        # Diagonal '\'
        for r in range(2, 14):
            rows[r] |= (1 << (15 - r)) | (1 << (14 - r))
    elif pattern_type == 2:
        # Diagonal '/'
        for r in range(2, 14):
            rows[r] |= (1 << r) | (1 << (r + 1))
    else:
        # Square '#'
        rows[4] |= 0x0FF0
        rows[11] |= 0x0FF0
        for r in range(4, 12):
            rows[r] |= 0x0810

    # Pack 16 rows into 32 bytes (big endian bits per row)
    packed = bytearray()
    for r in rows:
        packed.append((r >> 8) & 0xFF)
        packed.append(r & 0xFF)

    return bytes(packed)


_ETEN_ASC_PATH = r"D:\git\Fonts\iso\FILES\ASCFONT.15"
_ETEN_ASC_STRIDE = 15


def build_eten_ascii_block() -> bytes:
    """Builds the 256x16-byte ASCII glyph block (8x16, 1 byte/row, code-indexed)
    appended after the CJK glyphs in ZH16.DAT, sourced from the real ETen
    ASCFONT.15 (8x15, padded with a blank trailing row). Falls back to an
    all-blank block if the font file isn't available."""
    try:
        bank = Path(_ETEN_ASC_PATH).read_bytes()
    except OSError:
        return b"\x00" * (256 * 16)
    out = bytearray()
    for code in range(256):
        offset = code * _ETEN_ASC_STRIDE
        glyph = bank[offset : offset + _ETEN_ASC_STRIDE]
        if len(glyph) < _ETEN_ASC_STRIDE:
            glyph = glyph + b"\x00" * (_ETEN_ASC_STRIDE - len(glyph))
        out.extend(glyph)
        out.append(0)
    return bytes(out)


def build_zh_font(glyphs: list[str]) -> tuple[bytes, dict[str, Any]]:
    """Builds the ZH16.DAT binary and corresponding JSON mapping."""
    char_to_id: dict[str, int] = {}
    id_to_char: dict[int, str] = {}
    next_gid = 0
    for g in glyphs:
        if g not in char_to_id:
            # Never assign a glyph ID whose trail byte would land in
            # TRAIL_PART2 (0x80-0xDF). TEXTWRAP.C's line-wrap break-point
            # scan treats any byte in that range as a break point on the
            # (English-derived) assumption that it can only be a lead byte;
            # a trail byte that happens to share the range is indistinguishable
            # to it from a real lead byte, and its backward break-point search
            # walks byte-by-byte with no character-boundary tracking, so it
            # misreads such a trail byte as a break point and cuts the line
            # short there. Restricting every glyph to a TRAIL_PART1
            # (0x20-0x7E) trail byte makes 0x80-0xDF unambiguously
            # "lead byte" again, fixing this without touching TEXTWRAP.C.
            # This wastes 65 of every 160 ID slots per lead byte (9,120
            # usable of 15,360 total) -- still ample headroom.
            while next_gid % SLOTS_PER_LEAD >= 95:
                next_gid += 1
            char_to_id[g] = next_gid
            id_to_char[next_gid] = g
            next_gid += 1

    count = (max(id_to_char) + 1) if id_to_char else 0

    # Header: "ZHFN" (4), version 1 (u16), width 16 (u8), height 16 (u8), count (u16), base_lead 0x80 (u8), pad 5
    hdr = struct.pack("<4sHBBHB5s", b"ZHFN", 1, 16, 16, count, LEAD_MIN, b"\x00" * 5)
    body = bytearray()

    for gid in range(count):
        ch = id_to_char.get(gid)
        if ch is None:
            # Unused slot skipped above (trail byte would be in TRAIL_PART2).
            body.extend(b"\x00" * 32)
            continue
        bitmap = (
            render_glyph_from_eten(ch)
            or render_glyph_from_ttf(ch)
            or generate_synthetic_glyph(ch, gid)
        )
        body.extend(bitmap)

    meta = {
        "format": "ZH16_FONT",
        "version": 1,
        "glyph_width": 16,
        "glyph_height": 16,
        "glyph_count": count,
        "char_to_id": char_to_id,
        "glyphs": [id_to_char.get(i, "") for i in range(count)],
    }

    ascii_block = build_eten_ascii_block()

    return hdr + body + ascii_block, meta


def glyphs_from_translations(translated_dir: Path) -> list[str]:
    """Collects every unique CJK character actually used by translated
    (status == "translated") entries across all localization/translated/*.json
    files, so the glyph set grows from real translation work instead of a
    hand-picked demo list."""
    chars: dict[str, None] = {}
    for path in sorted(translated_dir.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for entry in data.get("entries", []):
            if entry.get("status") != "translated":
                continue
            for ch in entry.get("translation", ""):
                code = ord(ch)
                is_cjk_ideograph = 0x4E00 <= code <= 0x9FFF
                is_cjk_punctuation = 0x3000 <= code <= 0x303F
                is_fullwidth_form = 0xFF00 <= code <= 0xFFEF
                is_general_punct_dash_or_ellipsis = code in (0x2014, 0x2026)
                if is_cjk_ideograph or is_cjk_punctuation or is_fullwidth_form or is_general_punct_dash_or_ellipsis:
                    chars.setdefault(ch, None)
    return list(chars)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build ZH16.DAT and mapping table.")
    parser.add_argument("--output-font", type=Path, default=Path("ZH16.DAT"), help="Output font binary path")
    parser.add_argument("--output-map", type=Path, default=Path("zh_mapping.json"), help="Output JSON mapping path")
    parser.add_argument("--from-translations", type=Path, default=None,
                         help="Directory of localization/translated/*.json files to derive the glyph set from "
                              "(default: the built-in POC_GLYPHS demo list).")
    args = parser.parse_args()

    glyphs = glyphs_from_translations(args.from_translations) if args.from_translations else list(POC_GLYPHS)
    font_bin, meta = build_zh_font(glyphs)
    args.output_font.write_bytes(font_bin)
    args.output_map.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Generated {meta['glyph_count']} glyphs -> {args.output_font} ({len(font_bin)} bytes), {args.output_map}")


if __name__ == "__main__":
    main()
