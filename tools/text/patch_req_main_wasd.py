"""Legacy one-off repair for rebinding the walk-screen Camp button to T.

The canonical MenuPage build now declares this override in MENUPAGE.json and
applies it through menupage_translate.py. This script remains useful for
repairing an already-built test directory without rebuilding every menu file.

The 3D world loop (WORLDLP.C) resolves on-screen icon clicks and keyboard
shortcuts through the same MenuPage action ids in REQ_MAIN.DAT. Entry 8 is the
Camp (tent) icon and ships with action id 0x12, which is also the scan code for
the 'E' key -- so pressing 'E' or clicking the tent both opened Encamp.

The WASD/QE control scheme puts strafe-right on 'E'. To free 0x12 up we move the
Camp icon's action id to 0x14 (the 'T' scan code). After this patch:

  * clicking the tent icon returns 0x14  -> WORLDLP.C `case 0x14` -> encamp_run()
  * pressing 'T' matches entry 8         -> same encamp path
  * pressing 'E' matches no entry        -> raw 0x12 -> `case 0x12` -> strafe right

Only entry 8's u16 action id changes; the file length and every other field
stay byte-identical. Region-map screen (MAP.C / REQ_MAP.DAT) is a separate
dispatch and keeps 'E' = Encamp there.

Usage:
    python tools/text/patch_req_main_wasd.py

Reads scratchpad/pristine_menu/REQ_MAIN.DAT, writes
dist/test_v100_zh/req_main.dat (res_fopen prefers the loose file over the RMF).
"""

import struct
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "scratchpad" / "pristine_menu" / "REQ_MAIN.DAT"
DST = REPO / "dist" / "test_v100_zh" / "req_main.dat"

HEADER_SIZE = 0x1C
ENTRY_SIZE = 0x21
CAMP_ENTRY = 8
OLD_ACTION = 0x12  # 'E' scan code
NEW_ACTION = 0x14  # 'T' scan code


def main() -> int:
    data = bytearray(SRC.read_bytes())
    count = struct.unpack_from("<H", data, HEADER_SIZE)[0]
    if CAMP_ENTRY >= count:
        sys.exit(f"REQ_MAIN.DAT has only {count} entries; expected the Camp icon at {CAMP_ENTRY}")

    action_off = HEADER_SIZE + 2 + CAMP_ENTRY * ENTRY_SIZE + 2
    cur = struct.unpack_from("<H", data, action_off)[0]
    if cur == NEW_ACTION:
        print("already patched; nothing to do")
    elif cur != OLD_ACTION:
        sys.exit(f"entry {CAMP_ENTRY} action id is {cur:#x}, expected {OLD_ACTION:#x} -- aborting")
    else:
        struct.pack_into("<H", data, action_off, NEW_ACTION)
        print(f"entry {CAMP_ENTRY} action id {OLD_ACTION:#x} -> {NEW_ACTION:#x}")

    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_bytes(data)
    print(f"wrote {DST} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
