from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GMAIN = ROOT / "upstream/betrayal-at-krondor/bak/SRC/GAME/GMAIN.C"


def test_new_timeline_starts_before_first_chapter_cutscene() -> None:
    source = GMAIN.read_text(encoding="utf-8")
    main_at = source.index("void far main(")
    main = source[main_at:]
    assert main.index("msgsave_start_new();") < main.index(
        "gmain_play_chapter_cutscene(1, 1, 1);"
    )
    assert "msgsave_start_new();" not in source[:main_at]
