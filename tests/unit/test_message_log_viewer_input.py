from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MSGVIEW = ROOT / "upstream/betrayal-at-krondor/bak/SRC/SCREENS/MSGVIEW.C"


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
