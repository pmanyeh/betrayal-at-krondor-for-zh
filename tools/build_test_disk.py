"""Create a bootable FreeDOS raw disk image for 86Box testing."""

import os
import shutil
import struct
import subprocess
from pathlib import Path

# Paths
ROOT = Path("/mnt/d/git/betrayal-at-krondor-for-zh")
FREEDOS_IMG = Path("/home/pmanyeh/bak-toolchain/freedos/freedos.img")
OUT_IMG = ROOT / "scratchpad" / "evg-native-cjk-poc" / "krondor_evg.img"
DIST_DIR = ROOT / "dist" / "test_v100_zh"
POC_DIR = ROOT / "scratchpad" / "evg-native-cjk-poc"

MENV = os.environ.copy()
MENV["MTOOLS_SKIP_CHECK"] = "1"


def run_mtool(tool: str, *args: str) -> None:
    res = subprocess.run([tool, *args], env=MENV, capture_output=True)
    if res.returncode != 0:
        raise RuntimeError(f"{tool} failed: {res.stderr.decode('latin1')}")


def build_disk() -> None:
    print(f"Creating 128MB raw disk image at {OUT_IMG}...")
    OUT_IMG.parent.mkdir(parents=True, exist_ok=True)
    tmp_dir = ROOT / "scratchpad" / "evg-native-cjk-poc" / "_tmp_dos"
    tmp_dir.mkdir(parents=True, exist_ok=True)

    # 128 MB = 262080 sectors = 134184960 bytes (C=260, H=16, S=63)
    total_bytes = 134184960
    total_sectors = total_bytes // 512
    part_start_lba = 63
    part_sectors = total_sectors - part_start_lba

    data = bytearray(total_bytes)

    # Copy MBR bootstrap code from freedos.img (first 446 bytes)
    mbr_src = FREEDOS_IMG.read_bytes()
    data[:446] = mbr_src[:446]

    # Write MBR Partition Entry 1 at 0x1BE (446)
    # Boot indicator: 0x80 (Active)
    # Start CHS: H=1, S=1, C=0 -> 0x01, 0x01, 0x00
    # Type: 0x06 (FAT16B)
    # End CHS: H=15, S=63, C=259
    # Start LBA: 63
    # Sectors: part_sectors
    part_entry = struct.pack(
        "<BBBBBBBBII",
        0x80,        # bootable
        1, 1, 0,     # start CHS
        0x06,        # FAT16
        15, 63, 255, # end CHS
        part_start_lba,
        part_sectors,
    )
    data[446 : 446 + 16] = part_entry
    data[510:512] = b"\x55\xAA"
    OUT_IMG.write_bytes(data)

    # Extract 512 byte VBR bootsector from freedos.img
    bootsector_file = tmp_dir / "bootsector.bin"
    bootsector_file.write_bytes(mbr_src[32256 : 32256 + 512])

    target = f"{OUT_IMG}@@32256"
    print("Formatting FAT16 filesystem with mformat...")
    run_mtool(
        "mformat",
        "-i",
        target,
        "-h",
        "16",
        "-s",
        "63",
        "-T",
        "259",
        "-v",
        "KRONDOR",
        "-B",
        str(bootsector_file),
        "::",
    )

    print("Extracting FreeDOS system files from source image...")
    src_target = f"{FREEDOS_IMG}@@32256"

    for f in ["KERNEL.SYS", "COMMAND.COM"]:
        try:
            run_mtool("mcopy", "-i", src_target, f"::{f}", str(tmp_dir / f))
            print(f"Extracted {f}")
        except Exception as e:
            print(f"Warning extracting {f}: {e}")

    # Write custom FDCONFIG.SYS and FDAUTO.BAT
    config_sys = tmp_dir / "FDCONFIG.SYS"
    config_sys.write_text(
        "FILES=40\r\n"
        "BUFFERS=30\r\n"
        "DOS=HIGH,UMB\r\n",
        encoding="ascii",
    )

    autoexec_bat = tmp_dir / "FDAUTO.BAT"
    autoexec_bat.write_text(
        "@echo off\r\n"
        "cls\r\n"
        "echo ====================================================\r\n"
        "echo Betrayal at Krondor EVG Native CJK In-Game POC\r\n"
        "echo ====================================================\r\n"
        "KRONDOR.EXE\r\n",
        encoding="ascii",
    )

    # Gather all files to copy in batch
    files_to_copy = []
    for f in tmp_dir.glob("*"):
        if f.name != "bootsector.bin":
            files_to_copy.append(str(f))

    for gf in sorted(DIST_DIR.glob("*")):
        if gf.is_file():
            # Skip if we will overwrite with POC
            if gf.name.upper() not in ["KRONDOR.EXE", "VMCODE.OVL", "SX.OVL", "ZH16.DAT"]:
                files_to_copy.append(str(gf))

    # Add POC binaries
    poc_exe = tmp_dir / "KRONDOR.EXE"
    shutil.copy2(POC_DIR / "KRONDOR-EVG-NATIVE-POC.EXE", poc_exe)
    files_to_copy.append(str(poc_exe))

    poc_vmcode = tmp_dir / "VMCODE.OVL"
    shutil.copy2(POC_DIR / "VMCODE-EVG-NATIVE-POC.OVL", poc_vmcode)
    files_to_copy.append(str(poc_vmcode))

    poc_sx = tmp_dir / "SX.OVL"
    shutil.copy2(POC_DIR / "SX.OVL", poc_sx)
    files_to_copy.append(str(poc_sx))

    poc_zh16 = tmp_dir / "ZH16.DAT"
    shutil.copy2(ROOT / "localization" / "generated" / "ZH16.DAT", poc_zh16)
    files_to_copy.append(str(poc_zh16))

    print(f"Batch copying {len(files_to_copy)} files to FAT16 disk image...")
    run_mtool("mcopy", "-i", target, "-o", *files_to_copy, "::")

    shutil.rmtree(tmp_dir, ignore_errors=True)
    print(f"Disk build complete! Target: {OUT_IMG} ({OUT_IMG.stat().st_size} bytes)")


if __name__ == "__main__":
    build_disk()
