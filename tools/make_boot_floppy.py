"""Create a 1.44MB FreeDOS boot floppy that transfers execution to C:\KRONDOR.EXE."""

import os
import subprocess
from pathlib import Path

ROOT = Path("/mnt/d/git/betrayal-at-krondor-for-zh")
FREEDOS_SRC = Path("/home/pmanyeh/bak-toolchain/freedos/freedos.img")
FLOPPY_IMG = ROOT / "scratchpad" / "evg-native-cjk-poc" / "vm" / "boot.img"

MENV = os.environ.copy()
MENV["MTOOLS_SKIP_CHECK"] = "1"


def run_mtool(tool: str, *args: str) -> None:
    res = subprocess.run([tool, *args], env=MENV, capture_output=True)
    if res.returncode != 0:
        print(f"Notice: {tool} {args}: {res.stderr.decode('latin1', errors='ignore')}")


def main():
    print(f"Creating 1.44MB boot floppy at {FLOPPY_IMG}...")
    FLOPPY_IMG.write_bytes(b"\x00" * 1474560)

    # Format 1.44MB floppy
    run_mtool("mformat", "-i", str(FLOPPY_IMG), "-f", "1440", "-v", "BOOT", "::")

    # Extract kernel and command.com
    tmp_kernel = Path("/tmp/KERNEL.SYS")
    tmp_com = Path("/tmp/COMMAND.COM")
    run_mtool("mcopy", "-o", "-i", f"{FREEDOS_SRC}@@32256", "::KERNEL.SYS", str(tmp_kernel))
    run_mtool("mcopy", "-o", "-i", f"{FREEDOS_SRC}@@32256", "::COMMAND.COM", str(tmp_com))

    # Write AUTOEXEC.BAT
    autoexec = Path("/tmp/AUTOEXEC.BAT")
    autoexec.write_text(
        "@echo off\r\n"
        "echo Booting FreeDOS from Floppy...\r\n"
        "C:\r\n"
        "KRONDOR.EXE\r\n",
        encoding="ascii",
    )

    # Write CONFIG.SYS
    config = Path("/tmp/CONFIG.SYS")
    config.write_text(
        "FILES=40\r\n"
        "BUFFERS=30\r\n"
        "DOS=HIGH,UMB\r\n",
        encoding="ascii",
    )

    # Copy files to floppy
    run_mtool("mcopy", "-o", "-i", str(FLOPPY_IMG), str(tmp_kernel), "::KERNEL.SYS")
    run_mtool("mcopy", "-o", "-i", str(FLOPPY_IMG), str(tmp_com), "::COMMAND.COM")
    run_mtool("mcopy", "-o", "-i", str(FLOPPY_IMG), str(autoexec), "::AUTOEXEC.BAT")
    run_mtool("mcopy", "-o", "-i", str(FLOPPY_IMG), str(config), "::CONFIG.SYS")
    run_mtool("mcopy", "-o", "-i", str(FLOPPY_IMG), str(autoexec), "::FDAUTO.BAT")
    run_mtool("mcopy", "-o", "-i", str(FLOPPY_IMG), str(config), "::FDCONFIG.SYS")

    print("Boot floppy created successfully!")


if __name__ == "__main__":
    main()
