"""Compile VESAPOC.C using Borland C++ 3.1 in WSL2 FreeDOS toolchain."""

import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path("/mnt/d/git/betrayal-at-krondor-for-zh")
SRC_DIR = ROOT / "scratchpad" / "vesa-640x400-cjk-poc" / "src"
RUNTIME_DIR = ROOT / "scratchpad" / "vesa-640x400-cjk-poc" / "runtime"
ARTIFACTS_DIR = ROOT / "scratchpad" / "vesa-640x400-cjk-poc" / "artifacts"
BUILD_LOG = ARTIFACTS_DIR / "BUILD.LOG"

BC31_DIR = Path("/home/pmanyeh/bak-toolchain/bc31")
FREEDOS_IMG = Path("/home/pmanyeh/bak-toolchain/freedos/freedos.img")
BUILD_DISK = Path("/tmp/vesa_build.img")


def main():
    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    log_lines = []

    def log(msg: str):
        print(msg)
        log_lines.append(msg)

    log("=== 1. Preparing Build Disk with Borland C++ 3.1 ===")
    if BUILD_DISK.exists():
        BUILD_DISK.unlink()
    shutil.copy2(FREEDOS_IMG, BUILD_DISK)

    target = f"{BUILD_DISK}@@32256"
    env = os.environ.copy()
    env["MTOOLS_SKIP_CHECK"] = "1"

    # Copy BC31 files into BUILD_DISK
    log("Copying BC31 toolchain to build disk...")
    # Clean setup/packages
    subprocess.run(["mdel", "-i", target, "::SETUP.BAT"], env=env, capture_output=True)
    subprocess.run(["mdeltree", "-i", target, "::PACKAGES"], env=env, capture_output=True)

    # Create directories on build disk
    subprocess.run(["mmd", "-i", target, "::BORLAND"], env=env, capture_output=True)
    subprocess.run(["mmd", "-i", target, "::BORLAND/BIN"], env=env, capture_output=True)
    subprocess.run(["mmd", "-i", target, "::BORLAND/INCLUDE"], env=env, capture_output=True)
    subprocess.run(["mmd", "-i", target, "::BORLAND/LIB"], env=env, capture_output=True)
    subprocess.run(["mmd", "-i", target, "::BORLAND/INCLUDE/SYS"], env=env, capture_output=True)

    # Copy BCC.EXE, TLINK.EXE, C0L.OBJ, EMU.LIB, MATHL.LIB, CL.LIB, headers
    bin_files = ["BCC.EXE", "TLINK.EXE", "TASM.EXE", "CPP.EXE"]
    for bf in bin_files:
        src = BC31_DIR / "BIN" / bf
        if src.exists():
            subprocess.run(["mcopy", "-o", "-i", target, str(src), f"::BORLAND/BIN/{bf}"], env=env, check=True)

    # Copy includes
    inc_dir = BC31_DIR / "INCLUDE"
    for hf in inc_dir.glob("*.H"):
        subprocess.run(["mcopy", "-o", "-i", target, str(hf), f"::BORLAND/INCLUDE/{hf.name}"], env=env, check=True)
    for hf in (inc_dir / "SYS").glob("*.H"):
        subprocess.run(["mcopy", "-o", "-i", target, str(hf), f"::BORLAND/INCLUDE/SYS/{hf.name}"], env=env, check=True)

    # Copy libs
    lib_dir = BC31_DIR / "LIB"
    for lf in ["C0L.OBJ", "EMU.LIB", "MATHL.LIB", "CL.LIB"]:
        src = lib_dir / lf
        if src.exists():
            subprocess.run(["mcopy", "-o", "-i", target, str(src), f"::BORLAND/LIB/{lf}"], env=env, check=True)

    # Copy source files
    subprocess.run(["mcopy", "-o", "-i", target, str(SRC_DIR / "VESAPOC.C"), "::VESAPOC.C"], env=env, check=True)
    subprocess.run(["mcopy", "-o", "-i", target, str(SRC_DIR / "VBE.H"), "::VBE.H"], env=env, check=True)

    # Write BUILD.BAT
    build_bat = Path("/tmp/BUILD.BAT")
    build_bat.write_text(
        "@echo off\r\n"
        "SET PATH=C:\\BORLAND\\BIN;C:\\FREEDOS\\BIN\r\n"
        "BCC -ml -IC:\\BORLAND\\INCLUDE -LC:\\BORLAND\\LIB VESAPOC.C > BUILD.OUT 2>&1\r\n"
        "echo BUILD_DONE\r\n",
        encoding="ascii",
    )
    subprocess.run(["mcopy", "-o", "-i", target, str(build_bat), "::BUILD.BAT"], env=env, check=True)

    # Write FDAUTO.BAT to invoke BUILD.BAT
    auto_bat = Path("/tmp/FDAUTO.BAT")
    auto_bat.write_text(
        "@echo off\r\n"
        "CALL C:\\BUILD.BAT\r\n",
        encoding="ascii",
    )
    subprocess.run(["mcopy", "-o", "-i", target, str(auto_bat), "::FDAUTO.BAT"], env=env, check=True)

    log("=== 2. Running Borland C++ 3.1 in QEMU ===")
    cmd = [
        "qemu-system-i386",
        "-m", "16M",
        "-drive", f"file={BUILD_DISK},format=raw",
        "-nographic",
        "-serial", "mon:stdio",
        "-display", "none",
    ]
    log(f"Command: {' '.join(cmd)}")
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        stdout, stderr = proc.communicate(timeout=25)
        log(stdout)
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout, stderr = proc.communicate()
        log("QEMU timed out (expected after build finished)")

    log("=== 3. Extracting Build Outputs ===")
    tmp_out = Path("/tmp/BUILD.OUT")
    tmp_exe = Path("/tmp/VESAPOC.EXE")
    if tmp_out.exists(): tmp_out.unlink()
    if tmp_exe.exists(): tmp_exe.unlink()

    subprocess.run(["mcopy", "-o", "-i", target, "::BUILD.OUT", str(tmp_out)], env=env, capture_output=True)
    subprocess.run(["mcopy", "-o", "-i", target, "::VESAPOC.EXE", str(tmp_exe)], env=env, capture_output=True)

    build_out_text = tmp_out.read_text(encoding="latin1", errors="ignore") if tmp_out.exists() else "NO BUILD.OUT"
    log("Build output:")
    log(build_out_text)
    BUILD_LOG.write_text("\n".join(log_lines) + "\n" + build_out_text + "\n", encoding="utf-8")

    if not tmp_exe.exists() or tmp_exe.stat().st_size == 0:
        raise RuntimeError("BCC compilation failed to produce VESAPOC.EXE!")

    dst_runtime_exe = RUNTIME_DIR / "VESAPOC.EXE"
    dst_artifact_exe = ARTIFACTS_DIR / "VESAPOC.EXE"
    shutil.copy2(tmp_exe, dst_runtime_exe)
    shutil.copy2(tmp_exe, dst_artifact_exe)

    # Copy ZH16.DAT to runtime dir
    zh16_src = ROOT / "localization" / "generated" / "ZH16.DAT"
    shutil.copy2(zh16_src, RUNTIME_DIR / "ZH16.DAT")

    log(f"SUCCESS: Compiled VESAPOC.EXE ({dst_runtime_exe.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
