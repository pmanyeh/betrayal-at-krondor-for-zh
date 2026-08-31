"""Patches the six fixed hero names inside a .GAM game-state file (STARTUP.GAM
or TEMP.GAM) from English to their established Traditional Chinese glossary
translations.

The six names live in GameState::characterNames (bak/SRC/GAME/GMAIN.H), a
fixed char[6][10] block: each hero gets a 10-byte, NUL-padded slot, in the
fixed order Locklear, Gorath, Owyn, Pug, James, Patrus. The renderer
(font_draw_text_far, used by both the encampment roster screen and dialog
speaker labels) already handles the 0x80-0xDF Chinese lead-byte range, so no
engine change is needed -- this is a pure game-data patch, matching every
established Chinese glossary name (all of which fit within 9 bytes + NUL).

Usage:
    python tools/text/patch_character_names.py <in.gam> <out.gam>
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(REPO_ROOT / "tools" / "font"))
from build_font import encode_string  # noqa: E402

SLOT_WIDTH = 10

# Fixed CharacterId order (bak/SRC/GAME/GMAIN.H): Locklear, Gorath, Owyn,
# Pug, James, Patrus. Chinese names match localization/glossary/glossary.json.
HERO_NAMES = [
    ("Locklear", "洛克利爾"),
    ("Gorath", "戈拉斯"),
    ("Owyn", "歐文"),
    ("Pug", "帕格"),
    ("James", "詹姆士"),
    ("Patrus", "派特魯斯"),
]


def patch(data: bytes, char_to_id: dict[str, int]) -> bytes:
    data = bytearray(data)
    for eng, zh in HERO_NAMES:
        needle = eng.encode("ascii") + b"\x00"
        idx = data.find(needle)
        if idx == -1:
            raise ValueError(f"Could not find original name {eng!r} in file")
        slot = bytes(data[idx : idx + SLOT_WIDTH])
        # Some saves leave stale bytes after the terminating NUL instead of
        # zero-filling the rest of the fixed-width slot.  Those bytes are not
        # part of the C string and are safe to replace along with the slot.
        if slot[: len(eng) + 1] != needle:
            raise ValueError(
                f"Unexpected slot bytes for {eng!r} at offset {idx}: {slot!r} "
                "(expected a NUL-terminated name inside the 10-byte slot)"
            )
        encoded = encode_string(zh, char_to_id)
        if len(encoded) + 1 > SLOT_WIDTH:
            raise ValueError(f"{zh!r} ({len(encoded)} bytes + NUL) does not fit in {SLOT_WIDTH}-byte slot")
        new_slot = encoded + bytes(SLOT_WIDTH - len(encoded))
        data[idx : idx + SLOT_WIDTH] = new_slot
        print(f"  {eng:10s} (offset {idx:6d}) -> {zh}  ({len(encoded)} bytes + NUL padding)")
    return bytes(data)


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        raise SystemExit(1)
    in_path, out_path = sys.argv[1], sys.argv[2]

    mapping_path = REPO_ROOT / "localization" / "generated" / "zh_mapping.json"
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    char_to_id = mapping["char_to_id"]

    data = Path(in_path).read_bytes()
    patched = patch(data, char_to_id)
    assert len(patched) == len(data), "patch must not change file length"
    Path(out_path).write_bytes(patched)
    print(f"OK: wrote {out_path} ({len(patched)} bytes, unchanged length)")


if __name__ == "__main__":
    main()
