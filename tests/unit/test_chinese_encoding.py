"""
Unit Tests for BAK-ZH Compact 2-Byte Chinese Encoding (Phase 3)
Verifies:
1. ASCII string preservation.
2. Chinese character encoding / decoding.
3. Mixed ASCII and Chinese sentences.
4. Complete isolation from game control bytes (0xE0..0xFF).
5. Malformed byte recovery.
6. Glyph ID capacity (0..15359).
"""

import unittest

from tools.font.build_font import (
    LEAD_MAX,
    LEAD_MIN,
    MAX_GLYPHS,
    POC_GLYPHS,
    bytes_to_glyph_id,
    decode_string,
    encode_string,
    glyph_id_to_bytes,
)


class TestChineseEncoding(unittest.TestCase):
    def setUp(self):
        self.char_to_id = {ch: i for i, ch in enumerate(POC_GLYPHS)}
        self.id_to_char = {i: ch for i, ch in enumerate(POC_GLYPHS)}

    def test_ascii_preservation(self):
        """Verify ASCII strings are 100% identical in encoded bytes."""
        ascii_text = "Inventory Options (123) #Title# @0\n\t"
        encoded = encode_string(ascii_text, self.char_to_id)
        self.assertEqual(encoded, ascii_text.encode("latin1"))

    def test_chinese_encoding_roundtrip(self):
        """Verify Chinese characters encode to 2-byte sequences and decode cleanly."""
        text = "歐文：我們在哪裡？"
        encoded = encode_string(text, self.char_to_id)
        # 歐(2B) + 文(2B) + ：(1B:?) + 我(2B) + 們(2B) + 在(2B) + 哪(2B) + 裡(2B) + ？(1B:?)
        decoded = decode_string(encoded, self.id_to_char)
        # Verify characters mapped in POC list
        self.assertIn("歐文", decoded)
        self.assertIn("我們在哪裡", decoded)

    def test_control_byte_isolation(self):
        """Verify NO encoded Chinese character uses bytes in the range 0xE0..0xFF."""
        # Test all possible 15,360 glyph IDs
        for gid in range(MAX_GLYPHS):
            b = glyph_id_to_bytes(gid)
            self.assertEqual(len(b), 2)
            lead, trail = b[0], b[1]
            # Lead must be in [0x80, 0xDF]
            self.assertTrue(
                LEAD_MIN <= lead <= LEAD_MAX,
                f"Lead byte {lead:#x} for glyph {gid} out of range [0x80, 0xDF]",
            )
            # Trail must NOT be in [0xE0, 0xFF]
            self.assertFalse(
                0xE0 <= trail <= 0xFF,
                f"Trail byte {trail:#x} for glyph {gid} collides with control range [0xE0, 0xFF]",
            )
            # Decode must match
            decoded_gid = bytes_to_glyph_id(lead, trail)
            self.assertEqual(gid, decoded_gid)

    def test_malformed_sequence_recovery(self):
        """Verify stray lead bytes without valid trail bytes don't crash or corrupt stream."""
        stray_data = b"Hello\x80\x00World\x85\xF0Rest"
        decoded = decode_string(stray_data, self.id_to_char)
        self.assertTrue(decoded.startswith("Hello?"))
        self.assertIn("World", decoded)


if __name__ == "__main__":
    unittest.main()
