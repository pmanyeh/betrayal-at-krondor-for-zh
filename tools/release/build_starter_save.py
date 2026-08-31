"""Developer-side tool: build the optional "easier start" saves shipped in the
release bundle under a slot named "Plus" (see tools/release/starter_save/).

Two save points ship inside that one slot, matching the game's own
GAMES\\<slot>.G0N\\SAVE0N.GAM convention for multiple checkpoints within a
slot (see SRC/SCREENS/MAINMENU.C's `SAVE??.GAM` wildcard scanning):

  SAVE01.GAM -- built from this project's own archived QA save (real
                chapter-1 gameplay from this project's own testing), with
                only starting gold bumped up (see GOLD_OFFSET below).
  SAVE02.GAM -- the user's own separate real playthrough, further along than
                SAVE01, with only the character-name Chinese patch applied
                (tools/text/patch_character_names.py) -- gold and everything
                else about that playthrough is left exactly as played.

## Why the base for SAVE01 isn't just a patched copy of STARTUP.GAM

An earlier version of this script built SAVE01 from the pristine STARTUP.GAM
("New Game" template). That crashed on load ("cannot load gi block" / Null
pointer assignment, SRC/R3D/SCENE/PROXIM.C: proximity_table_load) when picked
from the in-game Load Game menu. `gmain_start_dispatch()` (SRC/GAME/GMAIN.C)
routes New Game (mode 2, reads STARTUP.GAM) and Load Game (mode 3, reads a
GAMES\\<slot>.G0N\\SAVE0N.GAM) through the exact same `savegame_read()`, so
the two paths *look* equivalent -- but empirically, STARTUP.GAM is only ever
exercised through the New Game path in the shipped game, and evidently isn't
in a state the generic Load Game path can safely resume from (most likely
something in the Actor pool / shared_inventory/ground_pile region that New
Game's own follow-up setup fixes up but Load Game assumes is already valid).

Rather than fully reverse-engineer that gap, SAVE01 instead starts from one
of this project's own already-proven-loadable QA saves -- already referenced
elsewhere in this project's history as a working Load Game save (see
tools/release/starter_save_base/verified_chapter1_save.GAM) -- and only
patches the single field it's meant to differ by: starting gold. That save's
character names are already Chinese-translated (all of this project's
archived QA saves are), so no name patch is needed for SAVE01.

## How the nParty_gold byte offset was determined

`SRC/GAME/STATE/SAVEGAME.C: savegame_write/read` write a 100-byte header
(90-byte g_abSaveFileHeader + nChapter + 3 bookmark fields + a 2-byte version
that must read back as 0x16), followed by a raw copy of TEMP.GAM, which is
GameState (SRC/GAME/GMAIN.H) serialized starting at TEMP.GAM offset 0. Since
`nChapter` (u16) is the first GameState field and `nParty_gold` (i32) is the
second with no compiler padding between them on this 16-bit target, that
places nParty_gold at absolute file offset 100 + 2 = 102, 4 bytes, signed
little-endian. Cross-validated three independent ways: (a) the header's own
duplicate copy of nChapter at offset 0x5a matches the GameState-blob copy at
offset 100 in every sample file; (b) the version field at offset 0x62 reads
back exactly 0x16 as SAVEGAME.C expects; (c) the value at offset 102 is 0 in
untouched STARTUP.GAM and increases plausibly with playthrough progress
across all 40 of this project's own archived QA saves under
dist/test_v100_zh/GAMES/.

Usage:
    python tools/release/build_starter_save.py
"""

from __future__ import annotations

import json
import struct
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools" / "text"))
from patch_character_names import patch as patch_character_names  # noqa: E402

STARTER_SAVE_BASE_DIR = REPO_ROOT / "tools" / "release" / "starter_save_base"
OUT_SLOT_DIR = REPO_ROOT / "tools" / "release" / "starter_save" / "GAMES" / "Plus.G01"

GOLD_OFFSET = 102
GOLD_SIZE = 4
STARTER_GOLD = 1000


def build_gold_boosted_save(base_save_path: Path, out_path: Path, starter_gold: int) -> None:
    """SAVE01: this project's own QA save, only starting gold changed."""
    data = bytearray(base_save_path.read_bytes())

    (original_gold,) = struct.unpack_from("<l", data, GOLD_OFFSET)
    if not (0 <= original_gold < starter_gold):
        raise SystemExit(
            f"{base_save_path} 的起始金幣是 {original_gold}，不在預期的「比 {starter_gold} 少」範圍內，"
            "先確認這還是原本挑選的那份基準存檔、offset 假設沒有被破壞。"
        )
    struct.pack_into("<l", data, GOLD_OFFSET, starter_gold)

    original = base_save_path.read_bytes()
    diff_offsets = [i for i in range(len(original)) if original[i] != data[i]]
    unexpected = [i for i in diff_offsets if not (GOLD_OFFSET <= i < GOLD_OFFSET + GOLD_SIZE)]
    if unexpected:
        raise SystemExit(f"拒絕寫出：除了金幣欄位還有其他 byte 被改到了：{unexpected[:10]}...")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(bytes(data))
    print(f"OK: {out_path} ({len(data)} bytes)")
    print(f"    起始金幣：{original_gold} -> {starter_gold}")


def build_name_patched_save(base_save_path: Path, out_path: Path, char_to_id: dict[str, int]) -> None:
    """SAVE02: the user's own separate playthrough, only names translated."""
    original = base_save_path.read_bytes()
    data = patch_character_names(original, char_to_id)

    diff_offsets = [i for i in range(len(original)) if original[i] != data[i]]
    name_region = range(159, 219)  # six 10-byte character-name slots
    unexpected = [i for i in diff_offsets if i not in name_region]
    if unexpected:
        raise SystemExit(f"拒絕寫出：除了姓名欄位還有其他 byte 被改到了：{unexpected[:10]}...")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(data)
    print(f"OK: {out_path} ({len(data)} bytes)")


def main() -> None:
    mapping = json.loads((REPO_ROOT / "localization" / "generated" / "zh_mapping.json").read_text(encoding="utf-8"))
    char_to_id = mapping["char_to_id"]

    build_gold_boosted_save(
        STARTER_SAVE_BASE_DIR / "verified_chapter1_save.GAM", OUT_SLOT_DIR / "SAVE01.GAM", STARTER_GOLD
    )
    build_name_patched_save(
        STARTER_SAVE_BASE_DIR / "own_playthrough_chapter1_save.GAM", OUT_SLOT_DIR / "SAVE02.GAM", char_to_id
    )


if __name__ == "__main__":
    main()
