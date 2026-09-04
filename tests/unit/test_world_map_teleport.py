import re
from pathlib import Path


FMAP_SOURCE = (
    Path(__file__).resolve().parents[2]
    / "upstream"
    / "betrayal-at-krondor"
    / "bak"
    / "SRC"
    / "SCREENS"
    / "FMAP.C"
)
MODAL_SCREEN_SOURCE = FMAP_SOURCE.with_name("MODALSCR.C")


def test_world_map_teleport_has_one_destination_per_named_place() -> None:
    source = FMAP_SOURCE.read_text(encoding="ascii")
    table = re.search(
        r"g_fmapTeleportDestinations\[33\]\s*=\s*\{(?P<body>.*?)\};",
        source,
        re.DOTALL,
    )

    assert table is not None
    records = re.findall(r"\{\s*(\d+)\s*,([^{}]+)\}", table.group("body"))
    assert len(records) == 33
    assert all(1 <= int(zone) <= 8 for zone, _ in records)


def test_world_map_teleport_requires_advanced_cheat_and_left_click() -> None:
    source = FMAP_SOURCE.read_text(encoding="ascii")

    assert "g_cfgKnockKnock != 0" in source
    assert "teleportMouseDown == 0" in source
    assert "mouse_button_pressed(0) != 0" in source
    assert "curTown >= 0" in source
    assert "fmap_teleport_queue(curTown)" in source


def test_world_map_teleport_destinations_include_corrected_safe_locations() -> None:
    source = FMAP_SOURCE.read_text(encoding="ascii")
    table = re.search(
        r"g_fmapTeleportDestinations\[33\]\s*=\s*\{(?P<body>.*?)\};",
        source,
        re.DOTALL,
    )

    assert table is not None
    records = re.findall(r"\{\s*([^{}]+?)\s*\}", table.group("body"))
    normalized = [re.sub(r"\s+", "", record) for record in records]
    assert normalized[18] == "4,13,12,13,17,0x4000"
    assert normalized[27] == "6,17,13,22,18,0x2000"


def test_pending_teleport_detects_a_tile_y_only_change() -> None:
    source = MODAL_SCREEN_SOURCE.read_text(encoding="latin-1")

    assert "spawn.bTileY != g_gameState.nPlayerTileY" in source
    assert "spawn.bTileY == g_gameState.nPlayerTileY" not in source
