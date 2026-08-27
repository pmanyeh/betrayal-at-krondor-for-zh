"""Simulate exact AMI BIOS CMOS checksum algorithm across 0x10..0x41."""

import struct
from pathlib import Path

nvr_dir = Path(r"d:\git\betrayal-at-krondor-for-zh\scratchpad\evg-native-cjk-poc\vm\nvr")
nvr_dir.mkdir(parents=True, exist_ok=True)

cmos = bytearray(128)

# RTC
cmos[0x0B] = 0x02
cmos[0x0D] = 0x80

# Diagnostic
cmos[0x0E] = 0x00
cmos[0x0F] = 0x00

# Standard CMOS
cmos[0x10] = 0x40  # Floppy A: 1.44MB
cmos[0x11] = 0x00
cmos[0x12] = 0xF0  # Drive C: 47
cmos[0x13] = 0x00
cmos[0x14] = 0x01  # 1 floppy, VGA
cmos[0x15] = 0x80  # 640 KB
cmos[0x16] = 0x02
cmos[0x17] = 0x00  # 3072 KB ext (for 4MB total)
cmos[0x18] = 0x0C
cmos[0x19] = 0x2F  # Drive C type 47
cmos[0x1A] = 0x00

# Drive C parameters: Cyl=65, Head=16, WP=65535, LZ=65, Sec=63, Ctrl=0
cmos[0x1B:0x1B+9] = struct.pack("<HBHHBB", 65, 16, 65535, 65, 63, 0)

# Extended memory registers (0x30..0x31)
cmos[0x30] = 0x00
cmos[0x31] = 0x0C

# Extended checksum (0x32..0x33) = sum of 0x30..0x31
ext_chk = (cmos[0x30] + cmos[0x31]) & 0xFFFF
cmos[0x32] = (ext_chk >> 8) & 0xFF
cmos[0x33] = ext_chk & 0xFF

# Clear checksum cells before sum
cmos[0x2E] = 0
cmos[0x2F] = 0

# AMI BIOS checksum loop (sum of registers 0x10..0x2D)
chk = 0
for reg in range(0x10, 0x2E):
    chk = (chk + cmos[reg]) & 0xFFFF

cmos[0x2E] = (chk >> 8) & 0xFF
cmos[0x2F] = chk & 0xFF

# Also write to all NVR files
for p in nvr_dir.glob("*.nvr"):
    p.write_bytes(cmos)
for name in ["asus386.nvr", "win486.nvr", "dtk386.nvr", "award495.nvr", "deskpro386.nvr"]:
    (nvr_dir / name).write_bytes(cmos)

print(f"Wrote NVR files (chk=0x{chk:04X}, ext_chk=0x{ext_chk:04X})")
