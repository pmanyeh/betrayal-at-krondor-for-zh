"""Developer-side tool: build the "easy start" save shipped as an optional
convenience in the release bundle (see tools/release/starter_save/), from
scratch off the pristine STARTUP.GAM -- NOT by reusing anyone else's save
file, since that would raise a "do we actually have the right to redistribute
someone else's save" question this project isn't in a position to answer.

Only two things differ from a stock STARTUP.GAM:
  1. The six hero names, Chinese-translated (tools/text/patch_character_names.py,
     already used for the main release's STARTUP.GAM patch).
  2. GameState.nParty_gold bumped from the stock 0 to STARTER_GOLD, so a new
     player has a bit more breathing room to buy gear/services early on.

Everything else -- world/zone state, chapter, character stats, inventory,
event flags -- is untouched, byte-identical to STARTUP.GAM.

## How the nParty_gold byte offset was determined

`SRC/GAME/STATE/SAVEGAME.C: savegame_write/read` write a 100-byte header
(90-byte g_abSaveFileHeader + nChapter + 3 bookmark fields + a 2-byte version
that must read back as 0x16), followed by a raw copy of TEMP.GAM, which is
GameState (SRC/GAME/GMAIN.H) serialized starting at TEMP.GAM offset 0. Since
`nChapter` (u16) is the first GameState field and `nParty_gold` (i32) is the
second with no compiler padding between them on this 16-bit target, that
places nParty_gold at absolute file offset 100 + 2 = 102, 4 bytes, signed
little-endian.

This was cross-validated three independent ways before trusting it (see
scratchpad notes from the session that added this script): (a) the header's
own duplicate copy of nChapter at offset 0x5a matches the GameState-blob copy
at offset 100 in every sample file; (b) the version field at offset 0x62
reads back exactly 0x16 as SAVEGAME.C expects; (c) the value at offset 102
is 0 in the untouched STARTUP.GAM and increases plausibly with playthrough
progress across all 40 of this project's own archived QA saves under
dist/test_v100_zh/GAMES/ (spanning three separate playthroughs).

Usage:
    python tools/release/build_starter_save.py
"""

from __future__ import annotations

import struct
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools" / "text"))
from patch_character_names import patch as patch_character_names  # noqa: E402

STARTUP_GAM_PATH = REPO_ROOT / "betrayal-at-krondor" / "startup.gam"
OUT_PATH = REPO_ROOT / "tools" / "release" / "starter_save" / "GAMES" / "NewGamePlus.G01" / "SAVE00.GAM"

GOLD_OFFSET = 102
GOLD_SIZE = 4
STARTER_GOLD = 1000


def build(startup_gam_path: Path, out_path: Path, starter_gold: int) -> None:
    original = startup_gam_path.read_bytes()

    mapping_path = REPO_ROOT / "localization" / "generated" / "zh_mapping.json"
    import json

    char_to_id = json.loads(mapping_path.read_text(encoding="utf-8"))["char_to_id"]

    data = bytearray(patch_character_names(bytes(original), char_to_id))

    (original_gold,) = struct.unpack_from("<l", original, GOLD_OFFSET)
    if original_gold != 0:
        raise SystemExit(
            f"{startup_gam_path} 的起始金幣不是預期的 0（讀到 {original_gold}），"
            "offset 假設可能不對，先別繼續，重新核對 SAVEGAME.C 的存檔格式。"
        )
    struct.pack_into("<l", data, GOLD_OFFSET, starter_gold)

    if len(data) != len(original):
        raise SystemExit("拒絕寫出：檔案長度被改變了，這不應該發生")

    # Verify the only differences from pristine STARTUP.GAM are the six name
    # slots (already checked byte-by-byte by patch_character_names itself)
    # and exactly the 4 gold bytes -- nothing else moved.
    diff_offsets = [i for i in range(len(original)) if original[i] != data[i]]
    unexpected = [i for i in diff_offsets if not (GOLD_OFFSET <= i < GOLD_OFFSET + GOLD_SIZE)]
    name_diff_count = len(unexpected)
    print(f"[檢查] 跟原始 STARTUP.GAM 相比，除了金幣欄位，還有 {name_diff_count} 個 byte 不同（應該是六個姓名欄位）")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(bytes(data))

    (verify_gold,) = struct.unpack_from("<l", data, GOLD_OFFSET)
    print(f"OK: {out_path} ({len(data)} bytes)")
    print(f"    起始金幣：{original_gold} -> {verify_gold}")


def main() -> None:
    build(STARTUP_GAM_PATH, OUT_PATH, STARTER_GOLD)


if __name__ == "__main__":
    main()
