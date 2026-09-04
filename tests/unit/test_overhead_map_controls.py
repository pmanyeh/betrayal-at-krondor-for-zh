import json
import re
from pathlib import Path

import pytest

from tools.release import package_release


REPO_ROOT = Path(__file__).resolve().parents[2]
MAP_SOURCE = (
    REPO_ROOT
    / "upstream"
    / "betrayal-at-krondor"
    / "bak"
    / "SRC"
    / "GAME"
    / "WORLD"
    / "MAP.C"
)


def test_overhead_map_keyboard_moves_refresh_menu_state() -> None:
    source = MAP_SOURCE.read_text(encoding="ascii")

    for action_id in (0x11, 0x1F, 0x1E, 0x20, 0x10, 0x12):
        match = re.search(
            rf"case 0x{action_id:x}:.*?break;",
            source,
            flags=re.DOTALL,
        )
        assert match is not None
        assert "redraw_menu = render_dirty = 1;" in match.group(0)


def test_camp_action_overrides_cover_walk_and_overhead_maps() -> None:
    catalog_path = REPO_ROOT / "localization" / "translated" / "MENUPAGE.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    overrides = {
        (item["file"], item["entry"]): (
            item["expected_action_id"],
            item["action_id"],
        )
        for item in catalog["action_overrides"]
    }

    assert overrides[("REQ_MAIN.DAT", 8)] == (0x12, 0x14)
    assert overrides[("REQ_MAP.DAT", 8)] == (0x12, 0x14)


def test_release_packaging_rejects_omitted_action_override_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    catalog_path = tmp_path / "MENUPAGE.json"
    catalog_path.write_text(
        json.dumps(
            {
                "action_overrides": [
                    {"file": "REQ_MAIN.DAT"},
                    {"file": "REQ_MAP.DAT"},
                ]
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(package_release, "MENUPAGE_CATALOG", catalog_path)
    monkeypatch.setattr(
        package_release,
        "_load_manifest",
        lambda _: {"deployed_loose_sha256": {"req_main.dat": "hash"}},
    )

    with pytest.raises(SystemExit, match="req_map.dat"):
        package_release.collect_menupage_files()
