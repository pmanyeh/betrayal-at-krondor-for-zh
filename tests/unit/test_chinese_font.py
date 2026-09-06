"""
Unit Tests for ZH16.DAT Chinese Font Format (Phase 3)
Verifies:
1. Header structure (Magic "ZHFN", version 1, 16x16, glyph count).
2. Bitmap alignment (32 bytes per glyph).
3. Binary parsing and data integrity.
"""

import struct
import json
import tempfile
import unittest
from pathlib import Path

from tools.font.build_font import POC_GLYPHS, build_zh_font, decode_string, encode_string
from tools.font.build_small_font import chars_from_ddx_small_text, chars_from_translations


class TestChineseFont(unittest.TestCase):
    def test_font_generation_and_header(self):
        """Build font for POC glyph set and verify binary header."""
        glyphs = list(POC_GLYPHS)
        font_data, meta = build_zh_font(glyphs)

        self.assertEqual(meta["glyph_count"], len(glyphs))
        self.assertEqual(meta["glyph_width"], 16)
        self.assertEqual(meta["glyph_height"], 16)

        # Expected size: 16 bytes header + glyph_count * 32 bytes CJK bitmaps
        # + a trailing 256-entry * 16 bytes ETen ASCII block (mixed-mode Latin glyphs).
        expected_size = 16 + len(glyphs) * 32 + 256 * 16
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

    def test_small_font_ddx_title_collection_excludes_body_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "DIAL_Z01.json").write_text(
                json.dumps(
                    {
                        "entries": [
                            {
                                "status": "translated",
                                "translation": "#城鎮標題#這些內文字形不應收錄",
                            },
                            {"status": "translated", "translation": "沒有標題的正文"},
                            {
                                "status": "translated",
                                "translation": "章節面板完整文字",
                                "notes": "Uses the chapter-banner 10x10 Chinese font path.",
                            },
                            {"status": "untranslated", "translation": "#忽略#正文"},
                        ]
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            chars = set(chars_from_ddx_small_text(root))
            self.assertEqual(chars, set("城鎮標題章節面板完整文字"))
            self.assertNotIn("內", chars)

    def test_generated_small_font_covers_every_small_ui_source(self):
        repo = Path(__file__).resolve().parents[2]
        translated = repo / "localization" / "translated"
        source_names = [
            "UI_HARDCODED.json",
            "KEYWORD.json",
            "CHARACTER_NAMES.json",
            "OBJINFO.json",
            "SPELLS.json",
            "MNAMES.json",
            "MENUPAGE.json",
        ]
        chars = set(chars_from_translations([translated / name for name in source_names]))
        chars.update(chars_from_ddx_small_text(translated))

        mapping = json.loads(
            (repo / "localization" / "generated" / "zh_mapping.json").read_text(encoding="utf-8")
        )["char_to_id"]
        font_data = (repo / "localization" / "generated" / "ZHSTAT.DAT").read_bytes()
        magic, version, width, height, count = struct.unpack_from("<4sHBBH", font_data)
        self.assertEqual((magic, version, width, height), (b"ZHSM", 1, 10, 10))
        entry_size = 2 + ((width + 7) // 8) * height
        glyph_ids = {
            struct.unpack_from("<H", font_data, 10 + i * entry_size)[0]
            for i in range(count)
        }
        missing = sorted(ch for ch in chars if mapping[ch] not in glyph_ids)
        self.assertEqual(missing, [], f"ZHSTAT.DAT is missing small-UI glyphs: {''.join(missing)}")

    def test_spellbook_not_learned_hardcoded_bytes(self):
        repo = Path(__file__).resolve().parents[2]
        mapping = json.loads(
            (repo / "localization" / "generated" / "zh_mapping.json").read_text(encoding="utf-8")
        )["char_to_id"]
        encoded = encode_string("尚未學習", mapping)
        self.assertEqual(encoded, bytes.fromhex("97 3b 82 21 8e 41 86 3a"))
        decoded = decode_string(encoded, {glyph_id: ch for ch, glyph_id in mapping.items()})
        self.assertEqual(decoded, "尚未學習")

    def test_spellbook_exit_hardcoded_bytes(self):
        repo = Path(__file__).resolve().parents[2]
        mapping = json.loads(
            (repo / "localization" / "generated" / "zh_mapping.json").read_text(encoding="utf-8")
        )["char_to_id"]
        encoded = encode_string("離開", mapping)
        self.assertEqual(encoded, bytes.fromhex("84 26 82 2c"))
        decoded = decode_string(encoded, {glyph_id: ch for ch, glyph_id in mapping.items()})
        self.assertEqual(decoded, "離開")

    def test_mouselook_toggle_hardcoded_bytes(self):
        repo = Path(__file__).resolve().parents[2]
        mapping = json.loads(
            (repo / "localization" / "generated" / "zh_mapping.json").read_text(encoding="utf-8")
        )["char_to_id"]
        on_enc = encode_string("滑鼠視角模式：開", mapping)
        self.assertEqual(on_enc, bytes.fromhex("8f 42 86 4b 8c 2b 8d 6b 81 67 8f 6b 87 5a 82 2c"))
        off_enc = encode_string("滑鼠視角模式：關", mapping)
        self.assertEqual(off_enc, bytes.fromhex("8f 42 86 4b 8c 2b 8d 6b 81 67 8f 6b 87 5a 85 6c"))

    def test_quicksave_notice_hardcoded_bytes(self):
        repo = Path(__file__).resolve().parents[2]
        mapping = json.loads(
            (repo / "localization" / "generated" / "zh_mapping.json").read_text(encoding="utf-8")
        )["char_to_id"]
        save_enc = encode_string("快速存檔完成", mapping)
        self.assertEqual(save_enc, bytes.fromhex("85 7b 8a 59 8c 33 97 30 82 51 82 52"))
        load_enc = encode_string("正在讀取快速存檔……", mapping)
        self.assertEqual(load_enc, bytes.fromhex("87 51 81 26 90 30 8a 40 85 7b 8a 59 8c 33 97 30 80 7e 80 7e"))


if __name__ == "__main__":
    unittest.main()
