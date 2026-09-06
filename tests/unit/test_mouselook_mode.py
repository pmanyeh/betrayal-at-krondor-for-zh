from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "upstream" / "betrayal-at-krondor" / "bak" / "SRC"
WORLDLP = ENGINE / "GAME" / "WORLD" / "WORLDLP.C"
MOUSE_ASM = ENGINE / "INPUT" / "MOUSE.ASM"
WCURSOR = ENGINE / "INPUT" / "WCURSOR.C"
UIWIDGET = ENGINE / "UI" / "UIWIDGET.C"
DIALOG = ENGINE / "DIALOG" / "DIALOG.C"
HOTSPOT = ENGINE / "GAME" / "ENC" / "HOTSPOT.C"
SCREEN = ENGINE / "GFX" / "SCREEN" / "SCREEN.C"


class TestMouseLookMode(unittest.TestCase):
    def test_mouse_look_is_optional_and_toggled_by_f2(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")

        self.assertIn("static int g_bMouseLookMode = 0;", source)
        self.assertIn("#define MOUSELOOK_TOGGLE_SCANCODE 0x3c", source)
        self.assertIn("g_bMouseLookMode = !g_bMouseLookMode;", source)

    def test_mouse_look_prefers_relative_motion_without_viewport_edge_lock(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")
        mouse_source = MOUSE_ASM.read_text(encoding="utf-8")

        self.assertIn("#define MOUSELOOK_YAW_PER_MICKEY 0x02", source)
        self.assertIn("#define MOUSELOOK_RELATIVE_TO_CURSOR_SCALE 4", source)
        self.assertIn("mouse_get_motion_delta(&dx, &dy);", source)
        self.assertIn("mov\tax,0bh", mouse_source)
        self.assertIn("g_mouse_x_mickeys - *last_mouse_x", source)
        self.assertIn(
            "mouse_set_cursor_clip_rect(0, 0, g_wScreen_width, g_wScreen_height);",
            source,
        )
        self.assertIn("*last_mouse_x = g_mouse_x_mickeys;", source)
        self.assertNotIn("MOUSELOOK_RECENTER_MARGIN", source)
        self.assertNotIn("short *edge_x, short *edge_y", source)
        self.assertNotIn("mouse_set_cursor_clip_rect(g_world_widget->viewport.x", source)
        self.assertIn("orientation.yaw -= (short)(dx * MOUSELOOK_YAW_PER_MICKEY);", source)
        self.assertIn("key_is_down(MOUSELOOK_CTRL_SCANCODE) == 0", source)

    def test_release_config_uses_relative_mouse_capture(self) -> None:
        config = (ROOT / "tools/release/dosbox_krondor.conf.template").read_text(
            encoding="utf-8"
        )

        self.assertIn("autolock=true", config)
        self.assertIn("autolock_feedback=none", config)
        self.assertIn("mouse_emulation=locked", config)

    def test_modal_and_event_entries_release_mouse_look_capture(self) -> None:
        world_source = WORLDLP.read_text(encoding="utf-8")
        dialog_source = DIALOG.read_text(encoding="utf-8")
        hotspot_source = HOTSPOT.read_text(encoding="utf-8")

        self.assertIn("void worldloop_mouselook_release_for_modal(void)", world_source)
        self.assertEqual(
            dialog_source.count("worldloop_mouselook_release_for_modal();"), 2
        )
        self.assertEqual(
            world_source.count("worldloop_mouselook_release_for_modal();"), 5
        )
        for event_entry in (
            "modalscreen_pending_scene_trans();",
            "evtcond_pty_dirty_flags_process();",
            "itemuse_ground_pile_open_inv();",
            "hotspotevt_activate_at_player();",
            "townscene_cheat_menu_screen();",
        ):
            self.assertRegex(
                world_source,
                r"worldloop_mouselook_release_for_modal\(\);\s+[^\n]*"
                + re.escape(event_entry),
            )
        self.assertNotRegex(
            world_source,
            r"worldloop_mouselook_release_for_modal\(\);\s+[^\n]*"
            r"hotspotevt_disp_pending_events\(\);",
        )
        self.assertEqual(
            hotspot_source.count("worldloop_mouselook_release_for_modal();"), 6
        )
        for modal_event in (
            "hotspotevt_load_record0_town(evt);",
            "hotspotevt_type1_encounter_run(evt, (int *)&wHaltFlag);",
            "hotspotevt_monst_load_speak(evt);",
            "hotspotevt_action_enter_town(evt);",
            "hotspotevt_trap_main_fire(evt, &wHaltFlag);",
            "hotspotevt_action_enter_zone(evt);",
        ):
            self.assertRegex(
                hotspot_source,
                r"worldloop_mouselook_release_for_modal\(\);\s+[^\n]*"
                + re.escape(modal_event),
            )

    def test_mouse_look_has_bounded_vertical_pitch(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")

        self.assertIn("#define MOUSELOOK_PITCH_PER_MICKEY 0x01", source)
        self.assertIn("#define MOUSELOOK_PITCH_LIMIT 0x800", source)
        self.assertIn(
            "g_nMouseLookPitchOffset - dy * MOUSELOOK_PITCH_PER_MICKEY", source
        )
        self.assertIn(
            "g_world_camera->base.orientation.pitch = g_nMouseLookBasePitch;", source
        )

    def test_mouse_look_keeps_the_classic_world_viewport(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")
        screen_source = SCREEN.read_text(encoding="utf-8")

        self.assertIn("screen_frame_sync_buffers_rect(0xb, 0x80);", source)
        self.assertIn("menupage_draw(g_pReqMainPage);", source)
        self.assertIn("uiwidget_compass_draw();", source)
        self.assertNotIn("g_bMouseLookImmersiveActive", source)
        self.assertNotIn("MOUSELOOK_COMPOSITE", source)
        self.assertNotIn("screen_frame_stretch_world", screen_source)
        self.assertNotIn("screen_frame_compose_world", screen_source)

    def test_mouse_look_remaps_wasd_and_e_only_for_keyboard_input(self) -> None:
        source = WORLDLP.read_text(encoding="utf-8")

        self.assertIn("action_id == 0x1e && key_is_down(0x1e) != 0", source)
        self.assertIn("action_id == 0x20 && key_is_down(0x20) != 0", source)
        self.assertIn("action_id == MOUSELOOK_INTERACT_SCANCODE &&", source)
        self.assertIn("action_id = 0xc0;", source)

    def test_center_interaction_reuses_world_cursor_dispatch(self) -> None:
        world_source = WORLDLP.read_text(encoding="utf-8")
        cursor_source = WCURSOR.read_text(encoding="utf-8")

        self.assertIn("wcursor_dispatch_hotspot_as_left_click(&target_copy)", world_source)
        self.assertIn("g_wMenuDragState = 1;", cursor_source)
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

    def test_mouse_look_toggle_notices_match_encoded_strings(self) -> None:
        world_source = WORLDLP.read_text(encoding="utf-8")

        self.assertIn(
            r'"\x8f\x42\x86\x4b\x8c\x2b\x8d\x6b\x81\x67\x8f\x6b\x87\x5a\x82\x2c"',
            world_source,
        )
        self.assertIn(
            r'"\x8f\x42\x86\x4b\x8c\x2b\x8d\x6b\x81\x67\x8f\x6b\x87\x5a\x85\x6c"',
            world_source,
        )
