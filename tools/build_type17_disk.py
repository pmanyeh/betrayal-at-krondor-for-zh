"""Create 40.5MB Type 17 disk image (C=977, H=5, S=17) with valid FAT16 formatting."""

import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path("/mnt/d/git/betrayal-at-krondor-for-zh")
FREEDOS_SRC = Path("/home/pmanyeh/bak-toolchain/freedos/freedos.img")
OUT_IMG = Path("/tmp/krondor_type17.img")
FINAL_IMG = ROOT / "scratchpad" / "evg-native-cjk-poc" / "vm" / "krondor_evg.img"
DIST_DIR = ROOT / "dist" / "test_v100_zh"
POC_DIR = ROOT / "scratchpad" / "evg-native-cjk-poc"

MENV = os.environ.copy()
MENV["MTOOLS_SKIP_CHECK"] = "1"


def run_cmd(*args: str) -> None:
    res = subprocess.run(args, env=MENV, capture_output=True)
    if res.returncode != 0:
        print(f"Notice: {args}: {res.stderr.decode('latin1', errors='ignore')}")


def main():
    total_sectors = 977 * 5 * 17  # 83045 sectors = 42519040 bytes
    print(f"Creating {total_sectors * 512} byte image...")
    OUT_IMG.write_bytes(b"\x00" * (total_sectors * 512))

    # Write MBR and partition table (Start=17, Size=83028)
    sfdisk_script = "17,83028,0x06,*\n"
    subprocess.run(
        ["sfdisk", "-C", "977", "-H", "5", "-S", "17", str(OUT_IMG)],
        input=sfdisk_script.encode("ascii"),
        capture_output=True,
    )

    # Format partition starting at sector 17 (17 * 512 = 8704)
    target = f"{OUT_IMG}@@8704"
    run_cmd("mformat", "-i", target, "-h", "5", "-n", "17", "-t", "976", "-v", "KRONDOR", "::")

    # Extract kernel and command.com from freedos.img
    tmp_kernel = Path("/tmp/KERNEL.SYS")
    tmp_com = Path("/tmp/COMMAND.COM")
    run_cmd("mcopy", "-o", "-i", f"{FREEDOS_SRC}@@32256", "::KERNEL.SYS", str(tmp_kernel))
    run_cmd("mcopy", "-o", "-i", f"{FREEDOS_SRC}@@32256", "::COMMAND.COM", str(tmp_com))

    run_cmd("mcopy", "-o", "-i", target, str(tmp_kernel), "::KERNEL.SYS")
    run_cmd("mcopy", "-o", "-i", target, str(tmp_com), "::COMMAND.COM")

    # Write AUTOEXEC.BAT
    autoexec = Path("/tmp/FDAUTO.BAT")
    autoexec.write_text(
        "@echo off\r\n"
        "cls\r\n"
        "echo ====================================================\r\n"
        "echo Betrayal at Krondor EVG Native CJK In-Game POC\r\n"
        "echo ====================================================\r\n"
        "KRONDOR.EXE\r\n",
        encoding="ascii",
    )
    run_cmd("mcopy", "-o", "-i", target, str(autoexec), "::FDAUTO.BAT")
    run_cmd("mcopy", "-o", "-i", target, str(autoexec), "::AUTOEXEC.BAT")

    # Write CONFIG.SYS
    config = Path("/tmp/FDCONFIG.SYS")
    config.write_text(
        "FILES=40\r\n"
        "BUFFERS=30\r\n"
        "DOS=HIGH,UMB\r\n",
        encoding="ascii",
    )
    run_cmd("mcopy", "-o", "-i", target, str(config), "::FDCONFIG.SYS")
    run_cmd("mcopy", "-o", "-i", target, str(config), "::CONFIG.SYS")

    # Copy game files
    skip_exts = {".wri", ".bmp", ".sol", ".hlp", ".txt", ".doc"}
    files_to_copy = []
    for f in DIST_DIR.iterdir():
        if f.is_file():
            if f.suffix.lower() in skip_exts:
                continue
            if ".pre-" in f.name or ".new." in f.name or "ZH_MAP" in f.name or "DDX_BUILD" in f.name:
                continue
            if f.name.upper() in ["KRONDOR.EXE", "VMCODE.OVL", "SX.OVL", "ZH16.DAT"]:
                continue
            files_to_copy.append(str(f))

    print(f"Copying {len(files_to_copy)} game files...")
    run_cmd("mcopy", "-o", "-i", target, *files_to_copy, "::")

    # Copy POC binaries
    print("Copying POC binaries...")
    run_cmd("mcopy", "-o", "-i", target, str(POC_DIR / "KRONDOR-EVG-NATIVE-POC.EXE"), "::KRONDOR.EXE")
    run_cmd("mcopy", "-o", "-i", target, str(POC_DIR / "VMCODE-EVG-NATIVE-POC.OVL"), "::VMCODE.OVL")
    run_cmd("mcopy", "-o", "-i", target, str(POC_DIR / "SX.OVL"), "::SX.OVL")
    run_cmd("mcopy", "-o", "-i", target, str(ROOT / "localization" / "generated" / "ZH16.DAT"), "::ZH16.DAT")

    FINAL_IMG.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(OUT_IMG, FINAL_IMG)
    print(f"Done! Final image size: {FINAL_IMG.stat().st_size} at {FINAL_IMG}")


if __name__ == "__main__":
    main()
