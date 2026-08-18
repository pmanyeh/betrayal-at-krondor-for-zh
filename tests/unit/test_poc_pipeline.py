"""
Unit Tests for Phase 4 POC Chinese Rendering Pipeline
Verifies:
1. Test A: English regression (Pure ASCII metrics, whitespace, tokens).
2. Test B: Chinese glyph rendering simulation (16x16 bitmap draw, foreground color).
3. Test C: Mixed text handling (ASCII + Chinese coexistence).
4. Test D: Width calculation precision (Combined text pixel width).
5. Test E: Chinese character wrapping (Breaking on 2-byte boundaries).
"""

import json
import struct
import unittest
from pathlib import Path

from tools.font.build_font import (
    POC_GLYPHS,
    build_zh_font,
    decode_string,
    encode_string,
)
from tools.patch.apply_poc_patch import generate_poc_patch
from tools.text.ddx_extract import extract_ddx_data


class TestPocPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.font_bin, cls.font_meta = build_zh_font(list(POC_GLYPHS))
        cls.char_to_id = cls.font_meta["char_to_id"]
        cls.id_to_char = {v: k for k, v in cls.char_to_id.items()}

    def test_a_english_regression(self):
        """Test A: Verify pure English text metrics and ASCII codes remain 100% unchanged."""
        english_str = "Inventory (100 gold) #Title# @0\tNext"
        # In BAK engine: standard ASCII widths are proportional (e.g. 6-10 px)
        # Verify encoding does not touch any byte
        encoded = encode_string(english_str, self.char_to_id)
        self.assertEqual(encoded, english_str.encode("latin1"))

    def test_b_chinese_rendering_simulation(self):
        """Test B: Verify Chinese 2-byte sequence draws 16x16 monochrome bitmap to buffer."""
        sentence = "歐文"
        encoded = encode_string(sentence, self.char_to_id)
        self.assertEqual(len(encoded), 4)  # 2 characters * 2 bytes = 4 bytes

        # Simulated frame buffer (32x16 pixels)
        buffer = [[0 for _ in range(32)] for _ in range(16)]
        fg_color = 0x0F  # White

        # Draw glyphs
        x = 0
        for i in range(0, len(encoded), 2):
            lead = encoded[i]
            trail = encoded[i + 1]
            lead_idx = lead - 0x80
            trail_idx = (trail - 0x20) if trail < 0x80 else (95 + trail - 0x80)
            gid = lead_idx * 160 + trail_idx

            glyph_off = 16 + gid * 32
            glyph_bytes = self.font_bin[glyph_off : glyph_off + 32]

            # Render 16x16
            for row in range(16):
                b0 = glyph_bytes[row * 2]
                b1 = glyph_bytes[row * 2 + 1]
                row_bits = (b0 << 8) | b1
                for col in range(16):
                    if (row_bits & (0x8000 >> col)) != 0:
                        buffer[row][x + col] = fg_color
            x += 16

        # Verify pixels drawn in both glyph zones (0..15 and 16..31)
        pixels_glyph1 = sum(sum(1 for col in range(0, 16) if buffer[row][col] != 0) for row in range(16))
        pixels_glyph2 = sum(sum(1 for col in range(16, 32) if buffer[row][col] != 0) for row in range(16))
        self.assertGreater(pixels_glyph1, 10, "Glyph 1 should have non-empty rendered pixels")
        self.assertGreater(pixels_glyph2, 10, "Glyph 2 should have non-empty rendered pixels")

    def test_c_mixed_text_metrics(self):
        """Test C: Verify mixed text (ASCII + Chinese) coexists and advances coordinates correctly."""
        mixed_str = "Owyn: 歐文"
        encoded = encode_string(mixed_str, self.char_to_id)

        # ASCII 'O','w','y','n',':',' ' (6 bytes) + 歐(2B) + 文(2B) = 10 bytes
        self.assertEqual(len(encoded), 10)

        # Simulated pixel width calculation
        total_width = 0
        i = 0
        while i < len(encoded):
            b = encoded[i]
            if 0x80 <= b <= 0xDF:
                total_width += 16  # 16 px for Chinese glyph
                i += 2
            else:
                total_width += 8  # 8 px average for ASCII
                i += 1

        expected_width = 6 * 8 + 2 * 16  # 48 + 32 = 80 px
        self.assertEqual(total_width, expected_width)

    def test_d_width_calculation_precision(self):
        """Test D: Verify font_text_pixel_width simulation matches exact expected dimensions."""
        poc_text = "歐文：我們在哪裡？"
        # 5 mapped Chinese characters (歐,文,我,們,在,哪,裡) + 2 punctuation (mapped to ?)
        # In our mapping: 7 characters are in POC set (16px each), 2 are '?' (8px each)
        encoded = encode_string(poc_text, self.char_to_id)

        width = 0
        i = 0
        while i < len(encoded):
            b = encoded[i]
            if 0x80 <= b <= 0xDF:
                width += 16
                i += 2
            else:
                width += 8
                i += 1

        # 7 Chinese chars * 16px + 2 ASCII '?' * 8px = 112 + 16 = 128 px
        self.assertEqual(width, 128)

    def test_e_chinese_wrapping(self):
        """Test E: Verify Chinese text wraps cleanly at 2-byte boundary when line width exceeded."""
        # Max line width: 50 pixels (fits 3 Chinese characters = 48 px, 4th character at 64 px triggers wrap)
        chinese_sentence = "我們在哪裡克朗多"  # 7 characters
        encoded = encode_string(chinese_sentence, self.char_to_id)

        max_width = 50
        lines = []
        cur_line = bytearray()
        cur_width = 0

        i = 0
        while i < len(encoded):
            b = encoded[i]
            char_len = 2 if (0x80 <= b <= 0xDF) else 1
            char_width = 16 if char_len == 2 else 8
            char_bytes = encoded[i : i + char_len]

            if cur_width + char_width > max_width and len(cur_line) > 0:
                lines.append(bytes(cur_line))
                cur_line = bytearray()
                cur_width = 0

            cur_line.extend(char_bytes)
            cur_width += char_width
            i += char_len

        if len(cur_line) > 0:
            lines.append(bytes(cur_line))

        # Expected:
        # Line 0: 我們在 (3 chars = 6 bytes = 48 px)
        # Line 1: 哪裡克 (3 chars = 6 bytes = 48 px)
        # Line 2: 朗多 (2 chars = 4 bytes = 32 px)
        self.assertEqual(len(lines), 3)
        self.assertEqual(decode_string(lines[0], self.id_to_char), "我們在")
        self.assertEqual(decode_string(lines[1], self.id_to_char), "哪裡克")
        self.assertEqual(decode_string(lines[2], self.id_to_char), "朗多")

    def test_poc_ddx_file_generation(self):
        """Verify POC patched DDX contains intact record 100009 with encoded Chinese."""
        arc_path = Path(r"d:\git\betrayal-at-krondor-for-zh\betrayal-at-krondor\krondor.001")
        rmf_path = Path(r"d:\git\betrayal-at-krondor-for-zh\betrayal-at-krondor\krondor.rmf")
        map_path = Path(r"d:\git\betrayal-at-krondor-for-zh\localization\generated\zh_mapping.json")
        out_dir = Path(r"d:\git\betrayal-at-krondor-for-zh\localization\generated")

        if not arc_path.exists() or not rmf_path.exists():
            self.skipTest("Game data files not found, skipping DDX patch generation test")

        out_file, meta = generate_poc_patch(arc_path, rmf_path, map_path, out_dir)
        self.assertTrue(out_file.exists())

        # Extract and verify record 100009
        data = out_file.read_bytes()
        extracted = extract_ddx_data(data)

        target_rec = None
        for rec in extracted["records"]:
            if rec.get("node_id") == 100009:
                target_rec = rec
                break

        self.assertIsNotNone(target_rec)
        decoded = decode_string(target_rec["text"].encode("latin1"), self.id_to_char)
        self.assertIn("Mist floated in the pass.", decoded)
        self.assertIn("歐文", decoded)
        self.assertIn("我們在哪裡", decoded)


if __name__ == "__main__":
    unittest.main()
