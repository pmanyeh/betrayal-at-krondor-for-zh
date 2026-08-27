"""Start 86Box for Gate A and monitor for FreeDOS / Krondor startup screen captures."""

import ctypes
from ctypes import wintypes
import subprocess
import time
from pathlib import Path
from PIL import Image

from win32_capture import capture_hwnd

ROOT = Path(__file__).resolve().parent.parent
VM_DIR = ROOT / "scratchpad" / "evg-native-cjk-poc" / "vm"
EXE_86BOX = Path(r"C:\Users\pmany\AppData\Local\Microsoft\WinGet\Packages\86Box.86Box_Microsoft.Winget.Source_8wekyb3d8bbwe\86Box.exe")
OUT_DIR = ROOT / "scratchpad" / "evg-native-cjk-poc"

user32 = ctypes.windll.user32


def find_86box_window():
    hwnd_found = []

    def enum_cb(hwnd, lparam):
        if user32.IsWindowVisible(hwnd):
            length = user32.GetWindowTextLengthW(hwnd)
            if length > 0:
                buff = ctypes.create_unicode_buffer(length + 1)
                user32.GetWindowTextW(hwnd, buff, length + 1)
                title = buff.value
                if "86box" in title.lower():
                    hwnd_found.append((hwnd, title))
        return True

    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
    user32.EnumWindows(EnumWindowsProc(enum_cb), 0)
    return hwnd_found


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Starting 86Box with Gate A VM at {VM_DIR}...")
    print(">>> USER ACTION: When 86Box window opens, please press F1 in the 86Box window to continue boot! <<<")

    proc = subprocess.Popen([str(EXE_86BOX), "-P", str(VM_DIR)])

    try:
        # Monitor for 120 seconds while user presses F1
        for sec in range(1, 121):
            time.sleep(1)
            hwnds = find_86box_window()
            if hwnds:
                hwnd, title = hwnds[0]
                img = capture_hwnd(hwnd)
                if img:
                    # Check if screen changed from BIOS blue screen
                    snap_path = OUT_DIR / f"gate_a_snap_{sec:03d}s.png"
                    img.save(snap_path)
                    if sec % 5 == 0:
                        print(f"  [{sec:03d}s] Monitoring 86Box window... (Captured {snap_path.name})")

    finally:
        print("Closing 86Box...")
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except Exception:
            proc.kill()
        print("86Box closed.")


if __name__ == "__main__":
    main()
