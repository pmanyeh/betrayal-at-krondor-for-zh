"""
Text Rendering Pipeline Simulation & Unit Tests (Phase 1)
Faithfully simulates the exact algorithms in FONT.C, TEXTWRAP.C, and DIALOG.C
to verify ASCII width, whitespace wrapping, control code filtering, and token expansion.
"""

import unittest


class MockFontMetrics:
    """Simulates FONT.C font slot 0 metrics (Standard 8x8 / proportional font)."""
    def __init__(self, base_char=32, glyph_count=96, default_width=6, height=8, proportional_widths=None):
        self.base_char = base_char
        self.glyph_count = glyph_count
        self.default_width = default_width
        self.height = height
        self.width_table = proportional_widths or {}
        self.tab_width = 32

    def glyph_metrics(self, ch: int) -> tuple[int, int]:
        """Replicates font_glyph_metrics(int ch, unsigned int *w, unsigned int *h) in FONT.C:322."""
        idx = ch - self.base_char
        if idx < 0 or idx >= self.glyph_count:
            if ch == 9:  # '\t'
                return (self.tab_width, 0)
            return (0, 0)
        width = self.width_table.get(ch, self.default_width)
        return (width, self.height)

    def text_pixel_width(self, text: str) -> int:
        """Replicates font_text_pixel_width(char far *str) in FONT.C:82."""
        total = 0
        for char in text:
            code = ord(char)
            idx = code - self.base_char
            if 0 <= idx < self.glyph_count:
                total += self.width_table.get(code, self.default_width)
        return total


def textwrap_is_break_point(text: str, line_start: int, pos: int) -> bool:
    """Replicates textwrap_is_break_point in TEXTWRAP.C:14."""
    if pos < 0 or pos >= len(text):
        return False
    ch = text[pos]
    if ch == ' ':
        return True
    if not ch.isalpha():
        return False
    if pos - line_start <= 3:
        return False
    # Check for ellipsis: ... followed by alpha
    if text[pos - 3:pos] == "...":
        return True
    return False


def textwrap_compute_lines(text: str, max_width: int, font: MockFontMetrics, max_lines: int = 90) -> list[tuple[int, int]]:
    """Replicates textwrap_compute_lines in TEXTWRAP.C:36."""
    lines = []
    line_start = 0
    count = 0
    length = len(text)

    while count < max_lines and line_start < length:
        pos = line_start
        line_width = 0
        no_break = True
        
        while pos < length and text[pos] != '\0' and text[pos] != '\n':
            w, h = font.glyph_metrics(ord(text[pos]))
            if line_width + w > max_width:
                break
            line_width += w
            if textwrap_is_break_point(text, line_start, pos):
                no_break = False
            pos += 1

        if pos < length and text[pos] != '\0' and text[pos] != '\n' and not no_break:
            # Exact C logic from TEXTWRAP.C:63-69
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

        if line_start < length and text[line_start] == '\n':
            line_start += 1
        else:
            while line_start < length and text[line_start] == ' ':
                line_start += 1

    return lines


def dialog_expand_tokens(text: str, speaker_names: list[str]) -> str:
    """Replicates token expansion in DIALOG.C:597."""
    output = []
    i = 0
    length = len(text)
    while i < length:
        if text[i] == '@':
            if i + 1 < length and text[i + 1].isdigit():
                idx = int(text[i + 1])
                name = speaker_names[idx] if idx < len(speaker_names) else ""
                output.append(name)
                i += 2
                continue
            else:
                output.append(speaker_names[0] if speaker_names else "")
                i += 1
                continue
        output.append(text[i])
        i += 1
    return "".join(output)


class TestTextPipelineSim(unittest.TestCase):
    def setUp(self):
        # Setup standard proportional font metrics (e.g. ' ' = 4px, 'i' = 3px, 'W' = 9px, default = 6px)
        widths = {
            ord(' '): 4,
            ord('i'): 3,
            ord('l'): 3,
            ord('W'): 9,
            ord('M'): 9,
            ord('.'): 3,
            ord(','): 3,
        }
        self.font = MockFontMetrics(base_char=32, glyph_count=96, default_width=6, height=8, proportional_widths=widths)

    def test_ascii_width_calculation(self):
        """Verify font_text_pixel_width matches character sum."""
        text = "Hello World"
        # H(6) + e(6) + l(3) + l(3) + o(6) + ' '(4) + W(9) + o(6) + r(6) + l(3) + d(6) = 58
        expected_width = 6 + 6 + 3 + 3 + 6 + 4 + 9 + 6 + 6 + 3 + 6
        self.assertEqual(self.font.text_pixel_width(text), expected_width)

    def test_control_codes_width_zero(self):
        """Verify control bytes (>= 0xE0 / 0xF0) produce 0 width in font_text_pixel_width."""
        text_with_ctrl = "Hello\xF0\x01 World\xF0\x00"
        # The control bytes \xF0 and \x01 and \x00 are out of [32, 128) range and must contribute 0 to width
        expected_width = self.font.text_pixel_width("Hello World")
        self.assertEqual(self.font.text_pixel_width(text_with_ctrl), expected_width)

    def test_line_wrapping_on_spaces(self):
        """Verify textwrap_compute_lines breaks words cleanly at whitespace."""
        text = "The quick brown fox jumps over the lazy dog"
        # Set max_width to fit roughly ~15-20 characters
        max_width = 80
        lines = textwrap_compute_lines(text, max_width, self.font)
        
        extracted_lines = [text[start:end] for start, end in lines]
        
        # Verify all words are preserved and lines fit within max_width
        for line in extracted_lines:
            line_width = self.font.text_pixel_width(line)
            self.assertLessEqual(line_width, max_width)

        # Reconstructed text without spaces at line breaks should equal the original words
        reconstructed = " ".join(extracted_lines)
        self.assertEqual(reconstructed, text)

    def test_explicit_newline_wrapping(self):
        """Verify '\n' forces immediate line break regardless of width."""
        text = "Line 1\nLine 2\nLine 3"
        lines = textwrap_compute_lines(text, 200, self.font)
        extracted = [text[start:end] for start, end in lines]
        self.assertEqual(extracted, ["Line 1", "Line 2", "Line 3"])

    def test_dialog_token_expansion(self):
        """Verify @0, @1 tokens are expanded into speaker names."""
        speakers = ["Owyn", "Locklear", "Gorath"]
        raw_dialog = "@0: Where are we, @1? Look at @2."
        expanded = dialog_expand_tokens(raw_dialog, speakers)
        self.assertEqual(expanded, "Owyn: Where are we, Locklear? Look at Gorath.")


if __name__ == "__main__":
    unittest.main()
