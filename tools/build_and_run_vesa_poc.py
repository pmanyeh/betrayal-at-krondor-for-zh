"""Build and run VESAPOC with Borland C++ 3.1 in DOSBox-X."""

import os
import shutil
import subprocess
import time
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
POC_DIR = ROOT / "scratchpad" / "vesa-640x400-cjk-poc"
SRC_DIR = POC_DIR / "src"
RUNTIME_DIR = POC_DIR / "runtime"
ARTIFACTS_DIR = POC_DIR / "artifacts"
CONF_PATH = POC_DIR / "dosbox-x-vesa-poc.conf"
EXE_DOSBOX = Path(r"D:\git\DOSBox-X-AI\dosbox-src\bin\x64\Release\dosbox-x.exe")


def build():
    print("=== 1. Building VESAPOC.EXE with BCC 3.1 ===")
    for f in [RUNTIME_DIR / "VESAPOC.EXE", ARTIFACTS_DIR / "VESAPOC.EXE", POC_DIR / "VESAPOC.OBJ", POC_DIR / "VESAPOC.EXE"]:
        if f.exists(): f.unlink()

    # Ensure runtime dependencies in root and runtime
    for d in [POC_DIR, RUNTIME_DIR]:
        shutil.copy2(ROOT / "localization" / "generated" / "ZH16.DAT", d / "ZH16.DAT")
        shutil.copy2(SRC_DIR / "FONT8X16.DAT", d / "FONT8X16.DAT")

    # Run build in DOSBox-X with CONF_PATH
    cmd = [
        str(EXE_DOSBOX),
        "-conf", str(CONF_PATH),
        "-c", "CALL DO_BUILD.BAT",
        "-c", "EXIT",
    ]
    proc = subprocess.run(cmd, cwd=str(POC_DIR), capture_output=True, text=True, timeout=20)
    time.sleep(1)

    exe_path = POC_DIR / "VESAPOC.EXE"
    if not exe_path.exists() or exe_path.stat().st_size == 0:
        exe_path = RUNTIME_DIR / "VESAPOC.EXE"

    if not exe_path.exists() or exe_path.stat().st_size == 0:
        raise RuntimeError("Build failed to produce VESAPOC.EXE!")

    shutil.copy2(exe_path, RUNTIME_DIR / "VESAPOC.EXE")
    shutil.copy2(exe_path, ARTIFACTS_DIR / "VESAPOC.EXE")
    print(f"Build SUCCESS: {exe_path.name} ({exe_path.stat().st_size} bytes)")


def run():
    print("\n=== 2. Running VESAPOC.EXE in DOSBox-X ===")
    shutil.copy2(CONF_PATH, ARTIFACTS_DIR / "dosbox-x-vesa-poc.conf")

    # Clean old outputs
    for fn in ["VESA.TXT", "FRAME.RAW", "PALETTE.RAW"]:
        for d in [POC_DIR, RUNTIME_DIR, ARTIFACTS_DIR]:
            p = d / fn
            if p.exists(): p.unlink()

    cmd = [
        str(EXE_DOSBOX),
        "-conf", str(CONF_PATH),
        "-c", "VESAPOC.EXE",
        "-c", "EXIT",
    ]

    proc = subprocess.run(cmd, cwd=str(POC_DIR), capture_output=True, text=True, timeout=20)
    print("DOSBox-X process finished.")

    # Move runtime generated files from POC_DIR or RUNTIME_DIR into artifacts
    for fn in ["VESA.TXT", "FRAME.RAW", "PALETTE.RAW"]:
        src = POC_DIR / fn
        if not src.exists():
            src = RUNTIME_DIR / fn
        if src.exists():
            dst = ARTIFACTS_DIR / fn
            shutil.copy2(src, dst)
            print(f"Copied {fn} to artifacts/ ({dst.stat().st_size} bytes)")

    # Readback generation from FRAME.RAW and PALETTE.RAW
    raw_path = ARTIFACTS_DIR / "FRAME.RAW"
    pal_path = ARTIFACTS_DIR / "PALETTE.RAW"

    if raw_path.exists() and raw_path.stat().st_size == 256000:
        raw_bytes = raw_path.read_bytes()
        img = Image.frombytes("L", (640, 400), raw_bytes)

        if pal_path.exists() and pal_path.stat().st_size == 768:
            pal_bytes = pal_path.read_bytes()
            pal_list = list(pal_bytes)
            if max(pal_list) <= 63:
                pal_list = [v * 4 for v in pal_list]
            img.putpalette(pal_list)
            img_rgb = img.convert("RGB")
        else:
            img_rgb = img.convert("RGB")

        # Save primary guest capture and readback PNG
        full_png = ARTIFACTS_DIR / "vesa-640x400-full.png"
        readback_png = ARTIFACTS_DIR / "vesa-640x400-readback.png"
        img_rgb.save(full_png)
        img_rgb.save(readback_png)
        print(f"Generated lossless guest capture: {full_png.name} (640x400)")

        # Closeup covering CONTROL & NATIVE CJK glyphs
        closeup_crop = img_rgb.crop((130, 30, 450, 110))
        closeup_png = ARTIFACTS_DIR / "vesa-640x400-native-cjk-closeup.png"
        closeup_crop.save(closeup_png)
        print(f"Generated lossless closeup: {closeup_png.name} {closeup_crop.size}")


if __name__ == "__main__":
    build()
    run()
