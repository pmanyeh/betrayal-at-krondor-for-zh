from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MSGVIEW = ROOT / "upstream/betrayal-at-krondor/bak/SRC/SCREENS/MSGVIEW.C"
WORLDLP = ROOT / "upstream/betrayal-at-krondor/bak/SRC/GAME/WORLD/WORLDLP.C"


def test_message_preview_is_indented_by_two_chinese_cells() -> None:
    source = MSGVIEW.read_text(encoding="utf-8")
    assert "textwrap_draw_aligned((long)body, 52, 58 + row * 40, 248" in source


def test_message_viewer_polls_and_refreshes_mouse_input() -> None:
    source = MSGVIEW.read_text(encoding="utf-8")
    assert "screen_cur_refr_during_long_op();" in source
    assert "mouse_button_pressed(0)" in source
    assert "mouse_button_pressed(1)" in source
    assert "screen_cursor_set_position(160, 100);" in source
    assert "key == MSGVIEW_MOUSE_RIGHT" in source
    assert "mouse_x < 160" in source


def test_consecutive_pages_of_the_same_speech_are_grouped() -> None:
    source = MSGVIEW.read_text(encoding="utf-8")
    assert "first->conversation == next->conversation" in source
    assert "first->speaker_id == next->speaker_id" in source
    assert "first->source_key == next->source_key" in source
    assert "*body + body_len" in source
    assert "selected = msgview_group_start(selected);" in source


def test_l_opens_message_log_from_world_exploration() -> None:
    source = WORLDLP.read_text(encoding="utf-8")
    assert "#define MESSAGE_LOG_SCANCODE 0x26" in source
    assert "case MESSAGE_LOG_SCANCODE:" in source
    assert "worldloop_mouselook_release(&mouselook_capture_active" in source
    assert "msgview_run();" in source
