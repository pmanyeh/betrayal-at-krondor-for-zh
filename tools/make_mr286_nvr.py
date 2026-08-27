"""Set up mr286.nvr with Floppy A: 1.44MB and Drive C: 32MB."""

import struct
from pathlib import Path

nvr_path = Path(r"d:\git\betrayal-at-krondor-for-zh\scratchpad\evg-native-cjk-poc\vm\nvr\mr286.nvr")
nvr_path.parent.mkdir(parents=True, exist_ok=True)

cmos = bytearray(128)

cmos[0x0B] = 0x02
cmos[0x0D] = 0x80

# Floppy configuration
cmos[0x10] = 0x40  # Drive A: 1.44MB 3.5"
cmos[0x11] = 0x00
cmos[0x12] = 0xF0  # Drive C: 47 (User type)
cmos[0x13] = 0x00
cmos[0x14] = 0x01  # 1 Floppy, VGA

# Memory
cmos[0x15] = 0x80  # 640K base
cmos[0x16] = 0x02
cmos[0x17] = 0x00  # 3072K ext
cmos[0x18] = 0x0C

cmos[0x19] = 0x2F  # Drive C ext type 47
cmos[0x1A] = 0x00

# Drive C parameters: Cyl=65, Head=16, WP=65535, LZ=65, Sec=63, Ctrl=0
cmos[0x1B:0x1B+9] = struct.pack("<HBHHBB", 65, 16, 65535, 65, 63, 0)

# Checksum over 0x10..0x2D
chk = sum(cmos[0x10:0x2E]) & 0xFFFF
cmos[0x2E] = (chk >> 8) & 0xFF
cmos[0x2F] = chk & 0xFF

# Ext mem (0x30..0x31)
cmos[0x30] = 0x00
cmos[0x31] = 0x0C

nvr_path.write_bytes(cmos)
print(f"Wrote {nvr_path}")
