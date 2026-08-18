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
        if ord(ch) < 0x80:
            # Standard ASCII (0..127)
            output.append(ord(ch))
        elif ch in char_to_id:
            output.extend(glyph_id_to_bytes(char_to_id[ch]))
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
    unique_glyphs = []
    for g in glyphs:
        if g not in char_to_id:
            gid = len(unique_glyphs)
            char_to_id[g] = gid
            id_to_char[gid] = g
            unique_glyphs.append(g)

    count = len(unique_glyphs)

    # Header: "ZHFN" (4), version 1 (u16), width 16 (u8), height 16 (u8), count (u16), base_lead 0x80 (u8), pad 5
    hdr = struct.pack("<4sHBBHB5s", b"ZHFN", 1, 16, 16, count, LEAD_MIN, b"\x00" * 5)
    body = bytearray()

    for gid, ch in enumerate(unique_glyphs):
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
        "glyphs": unique_glyphs,
    }

    ascii_block = build_eten_ascii_block()

    return hdr + body + ascii_block, meta


def main() -> None:
    parser = argparse.ArgumentParser(description="Build ZH16.DAT and mapping table.")
    parser.add_argument("--output-font", type=Path, default=Path("ZH16.DAT"), help="Output font binary path")
    parser.add_argument("--output-map", type=Path, default=Path("zh_mapping.json"), help="Output JSON mapping path")
    args = parser.parse_args()

    font_bin, meta = build_zh_font(list(POC_GLYPHS))
    args.output_font.write_bytes(font_bin)
    args.output_map.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Generated {meta['glyph_count']} glyphs -> {args.output_font} ({len(font_bin)} bytes), {args.output_map}")


if __name__ == "__main__":
    main()
