from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
CHARSCRN_SOURCE = (
    REPO_ROOT
    / "upstream"
    / "betrayal-at-krondor"
    / "bak"
    / "SRC"
    / "CHAR"
    / "CHARSCRN.C"
)


def test_spellbook_exit_button_is_drawn_and_clickable() -> None:
    source = CHARSCRN_SOURCE.read_text(encoding="utf-8")

    assert "charscreen_spellbook_draw_exit_button(0);" in source
    assert "charscreen_spellbook_draw_exit_button(1);" in source
    assert "cursor_x >= SPELLBOOK_EXIT_X" in source
    assert "cursor_y >= SPELLBOOK_EXIT_Y" in source
    assert "done = 1;" in source


def test_spellbook_description_reserves_the_button_row() -> None:
    source = CHARSCRN_SOURCE.read_text(encoding="utf-8")

    assert "#define SPELLBOOK_DOC_HEIGHT 0x90" in source
    assert "#define SPELLBOOK_EXIT_Y 0xb4" in source
    assert source.count("SPELLBOOK_DOC_WIDTH, SPELLBOOK_DOC_HEIGHT") == 2
