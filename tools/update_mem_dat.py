"""Update mem.dat on krondor_evg_gate_a.img to allow successful boot."""

import os
import struct
import subprocess
from pathlib import Path

ROOT = Path("/mnt/d/git/betrayal-at-krondor-for-zh")
IMG_PATH = ROOT / "scratchpad" / "evg-native-cjk-poc" / "vm" / "krondor_evg_gate_a.img"
TARGET = f"{IMG_PATH}@@32256"
TMP_MEM = Path("/tmp/mem.dat")

TMP_MEM.write_bytes(struct.pack("<I", 65536))

env = os.environ.copy()
env["MTOOLS_SKIP_CHECK"] = "1"

subprocess.run(["mcopy", "-o", "-i", TARGET, str(TMP_MEM), "::mem.dat"], env=env, check=True)
print("Updated mem.dat on disk image to 64K threshold.")
