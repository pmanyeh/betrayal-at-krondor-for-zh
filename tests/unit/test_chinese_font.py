"""
Unit Tests for ZH16.DAT Chinese Font Format (Phase 3)
Verifies:
1. Header structure (Magic "ZHFN", version 1, 16x16, glyph count).
2. Bitmap alignment (32 bytes per glyph).
3. Binary parsing and data integrity.
"""

import struct
import unittest

from tools.font.build_font import POC_GLYPHS, build_zh_font


class TestChineseFont(unittest.TestCase):
    def test_font_generation_and_header(self):
        """Build font for POC glyph set and verify binary header."""
        glyphs = list(POC_GLYPHS)
        font_data, meta = build_zh_font(glyphs)

        self.assertEqual(meta["glyph_count"], len(glyphs))
        self.assertEqual(meta["glyph_width"], 16)
        self.assertEqual(meta["glyph_height"], 16)

        # Expected size: 16 bytes header + glyph_count * 32 bytes
        expected_size = 16 + len(glyphs) * 32
        self.assertEqual(len(font_data), expected_size)

        # Verify Header unpacking
        magic, ver, w, h, count, base_lead, pad = struct.unpack_from("<4sHBBHB5s", font_data, 0)
        self.assertEqual(magic, b"ZHFN")
        self.assertEqual(ver, 1)
        self.assertEqual(w, 16)
        self.assertEqual(h, 16)
        self.assertEqual(count, len(glyphs))
        self.assertEqual(base_lead, 0x80)

    def test_glyph_bitmap_integrity(self):
        """Verify each 16x16 glyph bitmap has valid non-zero rows."""
        glyphs = list(POC_GLYPHS)
        font_data, _ = build_zh_font(glyphs)

        for i in range(len(glyphs)):
            offset = 16 + i * 32
            glyph_bytes = font_data[offset : offset + 32]
            self.assertEqual(len(glyph_bytes), 32)
            # Check non-empty
            self.assertTrue(any(b != 0 for b in glyph_bytes))


if __name__ == "__main__":
    unittest.main()
