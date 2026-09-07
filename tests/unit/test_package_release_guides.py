from pathlib import Path
import zipfile
import pytest

from tools.release.package_release import (
    PLAYER_GUIDES,
    make_zip,
    write_readme,
    write_player_guides,
    write_project_license,
)


def test_player_guide_templates_cover_requested_topics() -> None:
    template_dir = Path(__file__).resolve().parents[2] / "tools" / "release"
    guides = {
        output_name: (template_dir / template_name).read_text(encoding="utf-8")
        for template_name, output_name in PLAYER_GUIDES
    }

    assert "F5" in guides["中文按鍵說明.txt"]
    assert "F9" in guides["中文按鍵說明.txt"]
    assert "L                   直接開啟訊息紀錄" in guides["中文按鍵說明.txt"]
    assert "此模式下不能再啟用循路前進" in guides["中文按鍵說明.txt"]
    assert "同一人物被分頁顯示的連續文字會合為一筆" in guides["新增功能說明.txt"]
    assert "官方 v1.02 非光碟修補回植" in guides["新增功能說明.txt"]
    assert "快速存檔／讀檔" in guides["新增功能說明.txt"]
    assert "33 個有名稱的地點" in guides["中文按鍵說明.txt"]
    assert "完整世界地圖左鍵點擊 33 個有名稱的地點" in guides["新增功能說明.txt"]
    assert "33 個落點均已逐一" in guides["新增功能說明.txt"]
    assert "開啟滑鼠視角模式時會自動解除循路前進" in guides["新增功能說明.txt"]


def test_write_player_guides_uses_windows_friendly_text(tmp_path: Path) -> None:
    write_player_guides(tmp_path)

    for _, output_name in PLAYER_GUIDES:
        data = (tmp_path / output_name).read_bytes()
        assert data.startswith(b"\xef\xbb\xbf")
        assert b"\r\n" in data
        assert b"\n" not in data.replace(b"\r\n", b"")


def test_release_readme_covers_latest_features_and_uses_windows_text(tmp_path: Path) -> None:
    write_readme(tmp_path)

    data = (tmp_path / "README_安裝說明.txt").read_bytes()
    text = data.decode("utf-8-sig")
    assert data.startswith(b"\xef\xbb\xbf")
    assert b"\r\n" in data
    assert b"\n" not in data.replace(b"\r\n", b"")
    assert "按 L" in text
    assert "按 F5" in text
    assert "按 F9" in text
    assert ".GAM 與 .MLG 一起處理" in text
    assert "不能再次啟用循路前進" in text


def test_release_includes_project_license(tmp_path: Path) -> None:
    write_project_license(tmp_path)
    assert (tmp_path / "LICENSE").read_text(encoding="utf-8").startswith("MIT License")


def test_release_zip_excludes_python_cache_artifacts(tmp_path: Path) -> None:
    release_dir = tmp_path / "release"
    release_dir.mkdir()
    (release_dir / "README.txt").write_text("release", encoding="utf-8")
    cache_dir = release_dir / "__pycache__"
    cache_dir.mkdir()
    (cache_dir / "installer.cpython-312.pyc").write_bytes(b"cache")

    zip_path = make_zip(release_dir)
    with zipfile.ZipFile(zip_path) as archive:
        names = archive.namelist()
    assert "release/README.txt" in names
    assert not any("__pycache__" in name or name.endswith(".pyc") for name in names)


@pytest.mark.parametrize("name", ["SAVE01.GAM", "save01.mlg", "MSGWORK.MLG",
                                 "MLGNEW.GAM", "MLGOLD.MLG", "MLGTXN.DAT"])
def test_release_rejects_player_history_anywhere(tmp_path: Path, name: str) -> None:
    release_dir = tmp_path / "release"
    nested = release_dir / "misplaced"
    nested.mkdir(parents=True)
    player_file = nested / name
    player_file.write_bytes(b"private")
    archive = tmp_path / "release.zip"
    archive.write_bytes(b"previous archive")
    with pytest.raises(SystemExit, match="拒絕打包"):
        make_zip(release_dir)
    assert player_file.read_bytes() == b"private"
    assert archive.read_bytes() == b"previous archive"
