from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "upstream" / "betrayal-at-krondor" / "bak" / "SRC"
WORLDLP = ENGINE / "GAME" / "WORLD" / "WORLDLP.C"
WCURSOR = ENGINE / "INPUT" / "WCURSOR.C"
UIWIDGET = ENGINE / "UI" / "UIWIDGET.C"


class TestMouseLookMode(unittest.TestCase):
    def test_mouse_look_is_optional_and_toggled_by_f2(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")

        self.assertIn("static int g_bMouseLookMode = 0;", source)
        self.assertIn("#define MOUSELOOK_TOGGLE_SCANCODE 0x3c", source)
        self.assertIn("g_bMouseLookMode = !g_bMouseLookMode;", source)

    def test_mouse_look_recenters_mouse_and_turns_camera(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")

        self.assertIn("screen_cursor_set_position(center_x, center_y);", source)
        self.assertIn("#define MOUSELOOK_YAW_PER_MICKEY 0x08", source)
        self.assertIn("g_mouse_x_mickeys - (center_x << 2)", source)
        self.assertIn("orientation.yaw -= (short)(dx * MOUSELOOK_YAW_PER_MICKEY);", source)
        self.assertIn("key_is_down(MOUSELOOK_CTRL_SCANCODE) == 0", source)

    def test_mouse_look_has_bounded_vertical_pitch(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")

        self.assertIn("#define MOUSELOOK_PITCH_PER_MICKEY 0x06", source)
        self.assertIn("#define MOUSELOOK_PITCH_LIMIT 0x800", source)
        self.assertIn("g_mouse_y_mickeys - (center_y << 2)", source)
        self.assertIn("g_nWorldViewYawNormal = g_nMouseLookBasePitch;", source)

    def test_mouse_look_remaps_wasd_and_e_only_for_keyboard_input(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")

        self.assertIn("action_id == 0x1e && key_is_down(0x1e) != 0", source)
        self.assertIn("action_id == 0x20 && key_is_down(0x20) != 0", source)
        self.assertIn("action_id == MOUSELOOK_INTERACT_SCANCODE &&", source)
        self.assertIn("action_id = 0xc0;", source)

    def test_center_interaction_reuses_world_cursor_dispatch(self) -> None:
        world_source = WORLDLP.read_text(encoding="utf-8")
        cursor_source = WCURSOR.read_text(encoding="utf-8")

        self.assertIn("wcursor_dispatch_action_at(center_x, center_y)", world_source)
        self.assertIn("WorldHotspot *far wcursor_find_action_at", cursor_source)
        self.assertIn(
            "return wcursor_dispatch_action_at(screen_cursor_get_x(), screen_cursor_get_y());",
            cursor_source,
        )

    def test_mouse_look_draws_crosshair_and_selected_hotspot(self) -> None:
        world_source = WORLDLP.read_text(encoding="utf-8")
        widget_source = UIWIDGET.read_text(encoding="utf-8")

        self.assertIn("wcursor_find_action_at(center_x, center_y)", world_source)
        self.assertIn("worldloop_hotspot_outline_draw(&target->rect, 0xe);", world_source)
        self.assertIn("void uiwidget_aim_point_draw", widget_source)
