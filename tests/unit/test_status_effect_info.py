from pathlib import Path
import json
import re
import unittest

from tools.font.build_font import decode_string


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "upstream" / "betrayal-at-krondor" / "bak" / "SRC"
SPELLFX_C = ENGINE / "COMBAT" / "SPELL" / "SPELLFX.C"
SPELLFX_H = ENGINE / "COMBAT" / "SPELL" / "SPELLFX.H"
WORLDLP = ENGINE / "GAME" / "WORLD" / "WORLDLP.C"


class TestStatusEffectInfo(unittest.TestCase):
    def test_hardcoded_chinese_effect_descriptions_match_the_mapping(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")
        mapping = json.loads(
            (ROOT / "localization" / "generated" / "zh_mapping.json").read_text(
                encoding="utf-8"
            )
        )["char_to_id"]
        id_to_char = {glyph_id: ch for ch, glyph_id in mapping.items()}
        array = source.split("static char *g_apszEffectInfo[9] = {", 1)[1].split("};", 1)[0]
        literals = re.findall(r'"((?:\\x[0-9a-f]{2})+)"', array)

        decoded = []
        for literal in literals[:6]:
            encoded = bytes(int(pair, 16) for pair in re.findall(r"\\x([0-9a-f]{2})", literal))
            decoded.append(decode_string(encoded, id_to_char))
        self.assertEqual(
            decoded,
            [
                "龍息術：生成濃霧",
                "燭光術：在地下產生光亮",
                "星暮術：在地面產生光亮",
                "光影欺敵：使施法者看似莫瑞德人",
                "通解術：使施法者能讀懂莫瑞德文",
                "薩瑞格之嗅：察覺陷阱寶箱",
            ],
        )

    def test_hit_test_uses_the_same_active_glyph_sequence_as_the_caption(self) -> None:
        source = SPELLFX_C.read_text(encoding="utf-8")

        self.assertIn("int spellfx_event_caption_hit_test(int mouse_x, int mouse_y)", source)
        self.assertIn("buf[n++] = g_event_caption_glyph_table[i] + 1;", source)
        self.assertIn("x = 0xA0 - (font_text_width_ds(buf) >> 1);", source)
        self.assertIn("width = font_text_width_ds(glyph);", source)
        self.assertIn("mouse_x >= x && mouse_x < x + width", source)

    def test_remaining_time_reads_the_matching_world_timer(self) -> None:
        source = SPELLFX_C.read_text(encoding="utf-8")
        header = SPELLFX_H.read_text(encoding="utf-8")

        self.assertIn("long spellfx_event_remaining_ticks(int effect_id)", source)
        self.assertIn("entry->bKind == 2", source)
        self.assertIn("entry->wSub_id == (unsigned short)effect_id", source)
        self.assertIn("extern long spellfx_event_remaining_ticks(int effect_id);", header)

    def test_world_click_opens_a_modal_info_card_and_redraws_afterwards(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")

        self.assertIn("worldloop_effect_info_show(effect_id);", source)
        self.assertIn("mouselook_capture_active == 0", source)
        self.assertIn("redraw_menu = render_dirty = redraw_caption = 1;", source)
        self.assertIn("screen_frame_present();", source)
        self.assertIn("screen_input_poll_confirm_cancel() != 0", source)

    def test_time_is_rounded_up_and_formatted_in_game_minutes(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")

        self.assertIn("minutes = (ticks + 29L) / 30L;", source)
        self.assertIn("days = minutes / (24L * 60L);", source)
        self.assertIn("hours = (minutes / 60L) % 24L;", source)
        self.assertIn("mins = minutes % 60L;", source)


if __name__ == "__main__":
    unittest.main()
