"""Run VESAPOC.EXE in standard DOSBox-X release, capture evidence, and analyze results."""

import ctypes
from ctypes import wintypes
import json
import os
import shutil
import subprocess
import time
from pathlib import Path
from PIL import Image

from tools.win32_capture import capture_hwnd

ROOT = Path(__file__).resolve().parent.parent
POC_DIR = ROOT / "scratchpad" / "vesa-640x400-cjk-poc"
RUNTIME_DIR = POC_DIR / "runtime"
ARTIFACTS_DIR = POC_DIR / "artifacts"
CONF_PATH = POC_DIR / "dosbox-x-vesa-poc.conf"
EXE_DOSBOX = Path(r"D:\git\DOSBox-X-AI\dosbox-src\bin\x64\Release\dosbox-x.exe")

user32 = ctypes.windll.user32


def find_dosbox_window():
    hwnd_found = []

    def enum_cb(hwnd, lparam):
        if user32.IsWindowVisible(hwnd):
            length = user32.GetWindowTextLengthW(hwnd)
            if length > 0:
                buff = ctypes.create_unicode_buffer(length + 1)
                user32.GetWindowTextW(hwnd, buff, length + 1)
                title = buff.value
                if "dosbox-x" in title.lower() or "dosbox" in title.lower():
                    hwnd_found.append((hwnd, title))
        return True

    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
    user32.EnumWindows(EnumWindowsProc(enum_cb), 0)
    return hwnd_found


def main():
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    # Copy config to artifacts
    shutil.copy2(CONF_PATH, ARTIFACTS_DIR / "dosbox-x-vesa-poc.conf")

    print(f"Launching DOSBox-X with config at {CONF_PATH}...")
    cmd = [
        str(EXE_DOSBOX),
        "-conf", str(CONF_PATH),
        "-c", "VESAPOC.EXE",
        "-c", "EXIT",
    ]

    proc = subprocess.Popen(cmd)
    captured_window_path = ARTIFACTS_DIR / "vesa-640x400-window-snap.png"

    try:
        for sec in range(1, 10):
            time.sleep(1)
            hwnds = find_dosbox_window()
            if hwnds:
                hwnd, title = hwnds[0]
                img = capture_hwnd(hwnd)
                if img and img.size[0] >= 600:
                    img.save(captured_window_path)
                    print(f"  [{sec:02d}s] Captured window screenshot: {captured_window_path.name} {img.size}")
                    break

        proc.wait(timeout=15)
        print("DOSBox-X exited normally.")
    except Exception as ex:
        print(f"Waiting finished with: {ex}")
        try:
            proc.terminate()
        except Exception:
            pass

    time.sleep(0.5)

    # Move runtime generated files into artifacts
    for fn in ["VESA.TXT", "FRAME.RAW", "PALETTE.RAW"]:
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
            # Convert 6-bit DAC (0..63) to 8-bit RGB (0..255) if necessary
            pal_list = list(pal_bytes)
            # Check if values are in 0..63 range
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

        # Generate lossless closeup of CONTROL & NATIVE CJK glyphs
        # Control at (150, 40) to (240, 100); Native at (330, 40) to (390, 100)
        # Combined closeup covering (150, 35) to (400, 110)
        closeup_crop = img_rgb.crop((150, 35, 390, 105))
        closeup_png = ARTIFACTS_DIR / "vesa-640x400-native-cjk-closeup.png"
        closeup_crop.save(closeup_png)
        print(f"Generated lossless closeup: {closeup_png.name} {closeup_crop.size}")


if __name__ == "__main__":
    main()
