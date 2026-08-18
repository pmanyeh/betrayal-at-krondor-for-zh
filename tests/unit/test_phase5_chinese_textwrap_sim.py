"""
Phase 5 acceptance simulation: faithfully mirrors the Chinese-aware
FONT.C / TEXTWRAP.C algorithms (upstream/betrayal-at-krondor, post
commit 4b681d3) to deterministically exercise the Phase 5 acceptance
categories that are impractical to assert pixel-by-pixel from a live
DOSBox-X screenshot: ASCII only, Chinese only, mixed, punctuation,
long line, max line, malformed bytes, and the textwrap_draw_aligned
horizontal/vertical alignment and clipping arithmetic.

Byte strings stand in for the game's `char far *` / `unsigned char`
text buffers; every helper below is a line-for-line port of the C.
"""

import unittest

LEAD_MIN = 0x80
LEAD_MAX = 0xDF


class MockFontMetrics:
    """Port of FONT.C slot-0 metrics used by font_glyph_metrics/font_text_pixel_width."""

    def __init__(self, base_char=32, glyph_count=96, default_width=6, height=8, widths=None):
        self.base_char = base_char
        self.glyph_count = glyph_count
        self.default_width = default_width
        self.height = height
        self.width_table = widths or {}
        self.tab_width = 32

    def glyph_width(self, ch: int) -> int:
        idx = ch - self.base_char
        if idx < 0 or idx >= self.glyph_count:
            return self.tab_width if ch == 9 else 0
        return self.width_table.get(ch, self.default_width)


def font_glyph_metrics(ch: int, font: MockFontMetrics, mixed_zh_mode: bool) -> tuple[int, int]:
    """Port of font_glyph_metrics() in FONT.C:482."""
    c = ch & 0xFF
    if LEAD_MIN <= c <= LEAD_MAX:
        return (16, 16)
    if mixed_zh_mode and 0x20 <= c < 0x80:
        return (8, 16)
    return (font.glyph_width(c), font.height)


def font_text_pixel_width(text: bytes, font: MockFontMetrics, mixed_zh_mode: bool) -> int:
    """Port of font_text_pixel_width() in FONT.C:119, post-fix (4b681d3):
    a lead byte with no trailing byte before the string end contributes 0px,
    matching font_draw_text_far's draw-nothing behavior for that case."""
    total = 0
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if LEAD_MIN <= c <= LEAD_MAX:
            i += 1
            if i < n:
                i += 1
                total += 16
        elif mixed_zh_mode and 0x20 <= c < 0x80:
            i += 1
            total += 8
        else:
            total += font.glyph_width(c)
            i += 1
    return total


def textwrap_is_break_point(text: bytes, line_start: int, pos: int) -> bool:
    """Port of textwrap_is_break_point() in TEXTWRAP.C:14."""
    if pos < 0 or pos >= len(text):
        return False
    ch = text[pos]
    if ch == ord(' '):
        return True
    if LEAD_MIN <= ch <= LEAD_MAX:
        return True
    if not chr(ch).isalpha():
        return False
    if pos - line_start <= 3:
        return False
    return text[pos - 3:pos] == b"..."


def textwrap_compute_lines(
    text: bytes, max_width: int, font: MockFontMetrics, max_lines: int = 90,
    mixed_zh_mode: bool = False,
) -> list[tuple[int, int]]:
    """Port of textwrap_compute_lines() in TEXTWRAP.C:38, post-fix (4b681d3)."""
    lines: list[tuple[int, int]] = []
    line_start = 0
    count = 0
    n = len(text)

    def ch_at(p: int) -> int:
        return text[p] if 0 <= p < n else 0

    while count < max_lines and ch_at(line_start) != 0:
        pos = line_start
        line_width = 0
        no_break = True

        while ch_at(pos) not in (0, ord('\n')):
            c = ch_at(pos)
            if LEAD_MIN <= c <= LEAD_MAX:
                if ch_at(pos + 1) == 0:
                    pos += 1
                    break
                width = 16
                if max_width < line_width + width:
                    break
                line_width += width
                no_break = False
                pos += 2
            else:
                width, _height = font_glyph_metrics(c, font, mixed_zh_mode)
                if max_width < line_width + width:
                    break
                line_width += width
                if textwrap_is_break_point(text, line_start, pos):
                    no_break = False
                pos += 1

        if ch_at(pos) not in (0, ord('\n')) and not no_break:
            while pos != line_start and not textwrap_is_break_point(text, line_start, pos):
                pos -= 1
            while True:
                if pos == line_start:
                    break
                pos -= 1
                if not textwrap_is_break_point(text, line_start, pos):
                    break
            pos += 1

        lines.append((line_start, pos))
        count += 1
        line_start = pos

        if ch_at(line_start) == ord('\n'):
            line_start += 1
        else:
            while ch_at(line_start) == ord(' '):
                line_start += 1

    return lines


def textwrap_draw_aligned_offsets(
    text: bytes, max_width: int, max_height: int, line_spacing: int, flags: int,
    first_line: int, font: MockFontMetrics, mixed_zh_mode: bool,
) -> dict:
    """Port of the offset/clipping arithmetic in textwrap_draw_aligned()
    (TEXTWRAP.C:110), returning the computed values instead of drawing
    pixels, so alignment and pagination math can be asserted directly."""
    line_height = font.height
    if mixed_zh_mode and line_height < 16:
        line_height = 16

    lines = textwrap_compute_lines(text, max_width, font, 90, mixed_zh_mode)
    count = len(lines)

    lines_remaining = 0
    while max_height < (line_height + line_spacing) * ((count - first_line) - lines_remaining) - line_spacing:
        lines_remaining += 1
    if lines_remaining == 1:
        lines_remaining += 1

    lines_drawn = (count - lines_remaining) - first_line

    voff = 0
    if (flags & 0x20) or (flags & 0x10):
        voff = max_height - (line_height + line_spacing) * lines_drawn
        if flags & 0x10:
            voff //= 2

    draws = []
    fl = first_line
    v = voff
    while fl < count - lines_remaining:
        if v + line_height > max_height:
            break
        line_text = text[lines[fl][0]:lines[fl][1]]
        hoff = 0
        if (flags & 2) or (flags & 4):
            hoff = max_width - font_text_pixel_width(line_text, font, mixed_zh_mode)
            if flags & 2:
                hoff //= 2
        draws.append({"line": line_text, "hoff": hoff, "voff": v})
        v += line_height + line_spacing
        fl += 1

    return {
        "line_count": count,
        "lines_remaining": lines_remaining,
        "lines_drawn": lines_drawn,
        "draws": draws,
    }


def encode_zh(*char_codes: int) -> bytes:
    """Builds a two-byte lead/trail Chinese sequence from raw byte pairs,
    e.g. encode_zh(0x80, 0x22) for one glyph."""
    return bytes(char_codes)


class TestChineseWidthAndMetrics(unittest.TestCase):
    def setUp(self):
        self.font = MockFontMetrics(base_char=32, glyph_count=96, default_width=6, height=8)

    def test_ascii_only_width(self):
        text = b"Hi!"
        self.assertEqual(
            font_text_pixel_width(text, self.font, mixed_zh_mode=False),
            self.font.glyph_width(ord('H')) + self.font.glyph_width(ord('i')) + self.font.glyph_width(ord('!')),
        )

    def test_chinese_only_width_is_16px_per_glyph(self):
        # Two well-formed glyphs: lead 0x80/trail 0x22, lead 0x80/trail 0x23.
        text = encode_zh(0x80, 0x22, 0x80, 0x23)
        self.assertEqual(font_text_pixel_width(text, self.font, mixed_zh_mode=False), 32)

    def test_mixed_ascii_and_chinese_width(self):
        # In mixed mode, printable ASCII goes through the 8px ETen-ASCII path.
        text = b"(" + encode_zh(0x80, 0x22) + b")"
        width = font_text_pixel_width(text, self.font, mixed_zh_mode=True)
        self.assertEqual(width, 8 + 16 + 8)

    def test_malformed_dangling_lead_byte_contributes_zero_width(self):
        # A well-formed glyph followed by a lone lead byte at the very end of
        # the string (no trailing byte) must cost 0px, matching
        # font_draw_text_far which skips it and draws nothing.
        well_formed = encode_zh(0x80, 0x22)
        dangling = bytes([0x81])
        text = well_formed + dangling
        self.assertEqual(
            font_text_pixel_width(text, self.font, mixed_zh_mode=False),
            font_text_pixel_width(well_formed, self.font, mixed_zh_mode=False),
        )


class TestTextwrapCompute(unittest.TestCase):
    def setUp(self):
        widths = {ord(' '): 4, ord('i'): 3, ord('l'): 3, ord('W'): 9, ord('.'): 3}
        self.font = MockFontMetrics(base_char=32, glyph_count=96, default_width=6, height=8, widths=widths)

    def test_ascii_only_wraps_on_spaces(self):
        text = b"The quick brown fox jumps over the lazy dog"
        lines = textwrap_compute_lines(text, 80, self.font)
        for start, end in lines:
            self.assertLessEqual(font_text_pixel_width(text[start:end], self.font, False), 80)
        self.assertEqual(b" ".join(text[s:e] for s, e in lines), text)

    def test_chinese_only_wraps_by_glyph_count(self):
        # Five 16px glyphs; max_width 40 fits exactly two glyphs per line.
        glyphs = [encode_zh(0x80, 0x20 + i) for i in range(5)]
        text = b"".join(glyphs)
        lines = textwrap_compute_lines(text, 40, self.font, mixed_zh_mode=False)
        lengths = [e - s for s, e in lines]
        self.assertEqual(lengths, [4, 4, 2])  # 2+2+1 glyphs of 2 bytes each

    def test_mixed_line_uses_chinese_lead_byte_as_break_point(self):
        # A Chinese lead byte is itself always a valid break point
        # (textwrap_is_break_point), so English and Chinese can sit on the
        # same line and still wrap cleanly between them.
        text = b"Hi" + encode_zh(0x80, 0x22, 0x80, 0x23)
        self.assertTrue(textwrap_is_break_point(text, 0, 2))

    def test_punctuation_is_not_a_break_point_by_itself(self):
        text = b"wait...more"
        # '.' is not alpha, so it never counts as a break point on its own.
        dot_positions = [i for i, c in enumerate(text) if c == ord('.')]
        for pos in dot_positions:
            self.assertFalse(textwrap_is_break_point(text, 0, pos))

    def test_long_chinese_text_produces_multiple_lines(self):
        text = b"".join(encode_zh(0x80, 0x20 + (i % 90)) for i in range(40))
        lines = textwrap_compute_lines(text, 64, self.font, mixed_zh_mode=False)
        self.assertGreater(len(lines), 1)
        rebuilt = b"".join(text[s:e] for s, e in lines)
        self.assertEqual(rebuilt, text)

    def test_max_lines_caps_output(self):
        text = b"\n".join([b"line"] * 10)
        lines = textwrap_compute_lines(text, 200, self.font, max_lines=3)
        self.assertEqual(len(lines), 3)

    def test_malformed_dangling_lead_byte_ends_the_line_without_crashing(self):
        text = encode_zh(0x80, 0x22, 0x80, 0x23) + bytes([0x81])
        lines = textwrap_compute_lines(text, 999, self.font, mixed_zh_mode=False)
        self.assertEqual(len(lines), 1)
        start, end = lines[0]
        # The dangling lead byte at the tail is included in the line span
        # (so nothing after it is silently dropped from bookkeeping) but
        # contributes no drawn width, matching font_draw_text_far.
        self.assertEqual(end, len(text))
        self.assertEqual(
            font_text_pixel_width(text[start:end], self.font, False),
            font_text_pixel_width(text[start:end - 1], self.font, False),
        )

    def test_invalid_trail_byte_still_consumes_two_bytes(self):
        # A lead byte followed by a byte outside both trail ranges (e.g. a
        # control code) is still consumed as a pair by the width/wrap layer,
        # matching font_draw_zh_glyph which draws a blank 16px glyph for an
        # unrecognized combination rather than reinterpreting the second
        # byte as a new character.
        text = bytes([0x80, 0x01, ord('A')])
        lines = textwrap_compute_lines(text, 999, self.font, mixed_zh_mode=False)
        self.assertEqual(lines, [(0, 3)])


class TestTextwrapDrawAligned(unittest.TestCase):
    def setUp(self):
        self.font = MockFontMetrics(base_char=32, glyph_count=96, default_width=6, height=8)

    def test_left_aligned_has_zero_horizontal_offset(self):
        text = encode_zh(0x80, 0x22, 0x80, 0x23, 0x80, 0x24, 0x80, 0x25, 0x80, 0x26)
        result = textwrap_draw_aligned_offsets(
            text, max_width=200, max_height=100, line_spacing=1, flags=0,
            first_line=0, font=self.font, mixed_zh_mode=False,
        )
        self.assertEqual(result["draws"][0]["hoff"], 0)

    def test_center_aligned_chinese_line_is_centered(self):
        # 5 glyphs * 16px = 80px of text in a 200px-wide box: hoff should be
        # (200-80)//2 = 60, matching the (200-80)/2 the real hardware showed
        # centered under the portrait in the DOSBox-X capture.
        text = encode_zh(0x80, 0x22, 0x80, 0x23, 0x80, 0x24, 0x80, 0x25, 0x80, 0x26)
        result = textwrap_draw_aligned_offsets(
            text, max_width=200, max_height=100, line_spacing=1, flags=2,
            first_line=0, font=self.font, mixed_zh_mode=False,
        )
        self.assertEqual(result["draws"][0]["hoff"], (200 - 80) // 2)

    def test_right_aligned_chinese_line_hugs_the_right_edge(self):
        text = encode_zh(0x80, 0x22, 0x80, 0x23)
        result = textwrap_draw_aligned_offsets(
            text, max_width=100, max_height=100, line_spacing=1, flags=4,
            first_line=0, font=self.font, mixed_zh_mode=False,
        )
        self.assertEqual(result["draws"][0]["hoff"], 100 - 32)

    def test_vertical_center_uses_mixed_zh_line_height(self):
        # g_bMixedZhMode forces line_height to at least 16px even though the
        # ASCII font slot is only 8px tall (the exact bug fixed in 90be31b).
        text = encode_zh(0x80, 0x22)
        result = textwrap_draw_aligned_offsets(
            text, max_width=200, max_height=64, line_spacing=1, flags=0x10,
            first_line=0, font=self.font, mixed_zh_mode=True,
        )
        expected_voff = (64 - (16 + 1) * 1) // 2
        self.assertEqual(result["draws"][0]["voff"], expected_voff)

    def test_overflow_triggers_pagination_not_data_loss(self):
        # Five 16px-tall lines in a box that only fits two: clipping must
        # reduce what's drawn this pass (g_wTextWrapLinesRemaining) without
        # discarding the remaining lines from the line table itself.
        text = b"\n".join(encode_zh(0x80, 0x20 + i) for i in range(5))
        result = textwrap_draw_aligned_offsets(
            text, max_width=200, max_height=34, line_spacing=1, flags=0,
            first_line=0, font=self.font, mixed_zh_mode=False,
        )
        self.assertEqual(result["line_count"], 5)
        self.assertLess(len(result["draws"]), result["line_count"])
        self.assertGreater(result["lines_remaining"], 0)


if __name__ == "__main__":
    unittest.main()
