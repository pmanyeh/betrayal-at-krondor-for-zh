from pathlib import Path

from tools.release.package_release import PLAYER_GUIDES, write_player_guides


def test_player_guide_templates_cover_requested_topics() -> None:
    template_dir = Path(__file__).resolve().parents[2] / "tools" / "release"
    guides = {
        output_name: (template_dir / template_name).read_text(encoding="utf-8")
        for template_name, output_name in PLAYER_GUIDES
    }

    assert "F5" in guides["中文按鍵說明.txt"]
    assert "F9" in guides["中文按鍵說明.txt"]
    assert "官方 v1.02 非光碟修補回植" in guides["新增功能說明.txt"]
    assert "快速存檔／讀檔" in guides["新增功能說明.txt"]
    assert "33 個有名稱的地點" in guides["中文按鍵說明.txt"]
    assert "完整世界地圖左鍵點擊 33 個有名稱的地點" in guides["新增功能說明.txt"]
    assert "33 個落點均已逐一" in guides["新增功能說明.txt"]


def test_write_player_guides_uses_windows_friendly_text(tmp_path: Path) -> None:
    write_player_guides(tmp_path)

    for _, output_name in PLAYER_GUIDES:
        data = (tmp_path / output_name).read_bytes()
        assert data.startswith(b"\xef\xbb\xbf")
        assert b"\r\n" in data
        assert b"\n" not in data.replace(b"\r\n", b"")
