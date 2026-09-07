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

    def test_world_click_opens_a_nonblocking_timed_info_card(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")

        self.assertIn("#define EFFECT_INFO_TICKS 0xb4", source)
        self.assertIn("effect_info_id = effect_id;", source)
        self.assertIn("effect_info_deadline = g_timer_ticks + EFFECT_INFO_TICKS;", source)
        self.assertIn("worldloop_effect_info_draw(effect_info_id);", source)
        self.assertIn("mouselook_capture_active == 0", source)
        self.assertIn("g_timer_ticks >= effect_info_deadline", source)
        self.assertNotIn("static void worldloop_effect_info_show", source)
        self.assertNotRegex(
            source,
            r"worldloop_effect_info_draw\(int effect_id\).*?for \(;;\)",
        )

    def test_added_world_notices_use_standard_yellow_with_a_shadow(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")

        self.assertIn("#define NOTICE_TEXT_COLOR 0x0a", source)
        self.assertIn("#define NOTICE_SHADOW_COLOR 1", source)
        self.assertEqual(source.count("NOTICE_TEXT_COLOR"), 4)
        self.assertEqual(source.count("NOTICE_SHADOW_COLOR"), 4)
        self.assertEqual(
            source.count(
                "uiwidget_draw_text_shadowed(text, NOTICE_SHADOW_COLOR, "
                "NOTICE_TEXT_COLOR"
            ),
            1,
        )
        self.assertIn(
            "uiwidget_draw_text_shadowed(time_text, NOTICE_SHADOW_COLOR, "
            "NOTICE_TEXT_COLOR",
            source,
        )
        self.assertIn(
            "uiwidget_draw_text_shadowed(g_apszEffectInfo[effect_id], "
            "NOTICE_SHADOW_COLOR,\n                                NOTICE_TEXT_COLOR",
            source,
        )
        self.assertNotIn("uiwidget_draw_text_shadowed(text, 0x33, 1", source)
        self.assertNotIn("NOTICE_TEXT_COLOR, NOTICE_SHADOW_COLOR", source)

    def test_time_is_rounded_up_and_formatted_in_game_minutes(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")

        self.assertIn("minutes = (ticks + 29L) / 30L;", source)
        self.assertIn("days = minutes / (24L * 60L);", source)
        self.assertIn("hours = (minutes / 60L) % 24L;", source)
        self.assertIn("mins = minutes % 60L;", source)


if __name__ == "__main__":
    unittest.main()
