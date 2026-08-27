"""Generate a valid award495.nvr with Drive C preconfigured and valid checksum."""

import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NVR_PATH = ROOT / "scratchpad" / "evg-native-cjk-poc" / "vm" / "nvr" / "award495.nvr"


def main():
    cmos = bytearray(128)

    # Standard RTC registers
    cmos[0x00] = 0x00  # Sec
    cmos[0x02] = 0x00  # Min
    cmos[0x04] = 0x12  # Hour
    cmos[0x06] = 0x02  # Day of week
    cmos[0x07] = 0x25  # Day
    cmos[0x08] = 0x08  # Month
    cmos[0x09] = 0x26  # Year
    cmos[0x0A] = 0x26  # Status A
    cmos[0x0B] = 0x02  # Status B
    cmos[0x0C] = 0x00  # Status C
    cmos[0x0D] = 0x80  # Status D (battery OK)
    cmos[0x0E] = 0x00  # Diagnostic status (0 = no error)
    cmos[0x0F] = 0x00  # Shutdown code

    # Equipment & Memory
    cmos[0x10] = 0x00  # Floppy (None)
    cmos[0x11] = 0x00  # Reserved
    cmos[0x12] = 0xF0  # Hard Disk: Drive C = Type 47 (User), Drive D = None
    cmos[0x13] = 0x00  # Advanced setup
    cmos[0x14] = 0x21  # Equipment: 1 FDD, 80x25 color, x87 present/configured

    # Base Memory (640K = 0x0280)
    cmos[0x15] = 0x80
    cmos[0x16] = 0x02

    # Extended Memory (3072K = 0x0C00)
    cmos[0x17] = 0x00
    cmos[0x18] = 0x0C

    # Extended drive types
    cmos[0x19] = 0x2F  # Drive C type = 47 (0x2F)
    cmos[0x1A] = 0x00  # Drive D type = 0

    # User Defined Drive 1 (Type 47): 65 Cyl, 16 Heads, 63 Sectors
    # In Award BIOS:
    # 0x1B: Cylinders low
    # 0x1C: Cylinders high (65 = 0x0041)
    # 0x1D: Heads (16 = 0x10)
    # 0x1E: Write Precomp low (0xFF)
    # 0x1F: Write Precomp high (0xFF)
    # 0x20: Landing Zone low (0x41)
    # 0x21: Landing Zone high (0x00)
    # 0x22: Sectors (63 = 0x3F)
    cmos[0x1B] = 0x41
    cmos[0x1C] = 0x00
    cmos[0x1D] = 0x10
    cmos[0x1E] = 0xFF
    cmos[0x1F] = 0xFF
    cmos[0x20] = 0x41
    cmos[0x21] = 0x00
    cmos[0x22] = 0x3F

    # Award BIOS specific flags
    cmos[0x23] = 0x00
    cmos[0x24] = 0x00
    cmos[0x25] = 0x00

    # Extended Memory size duplicates for 16MB+
    cmos[0x30] = 0x00
    cmos[0x31] = 0x0C
    cmos[0x32] = 0x20  # Century (20)
    cmos[0x33] = 0x00

    # Calculate standard CMOS checksum for bytes 0x10..0x2D
    csum = sum(cmos[0x10:0x2E]) & 0xFFFF
    cmos[0x2E] = (csum >> 8) & 0xFF
    cmos[0x2F] = csum & 0xFF

    NVR_PATH.parent.mkdir(parents=True, exist_ok=True)
    NVR_PATH.write_bytes(bytes(cmos))
    print(f"Generated valid award495.nvr at {NVR_PATH} (Checksum: 0x{csum:04X})")


if __name__ == "__main__":
    main()
