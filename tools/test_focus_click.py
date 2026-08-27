"""Click titlebar to ensure real OS focus, then send F1."""

import ctypes
from ctypes import wintypes
import subprocess
import time
from pathlib import Path
import pyautogui

from win32_capture import capture_hwnd
from test_sendinput import send_scancode

pyautogui.FAILSAFE = False

ROOT = Path(__file__).resolve().parent.parent
VM_DIR = ROOT / "scratchpad" / "evg-native-cjk-poc" / "vm"
EXE_86BOX = Path(r"C:\Users\pmany\AppData\Local\Microsoft\WinGet\Packages\86Box.86Box_Microsoft.Winget.Source_8wekyb3d8bbwe\86Box.exe")
OUT_DIR = ROOT / "scratchpad" / "evg-native-cjk-poc"

user32 = ctypes.windll.user32


def main():
    proc = subprocess.Popen([str(EXE_86BOX), "-P", str(VM_DIR)])
    try:
        print("Waiting 5s for Award BIOS to reach F1 prompt...")
        time.sleep(5)

        hwnd = user32.FindWindowW(None, "vm - 86Box 6.0 [build 9001]")
        if hwnd:
            rect = wintypes.RECT()
            user32.GetWindowRect(hwnd, ctypes.byref(rect))

            # Click titlebar
            tx = rect.left + 150
            ty = rect.top + 15
            print(f"Clicking titlebar at ({tx}, {ty})...")
            pyautogui.click(tx, ty)
            time.sleep(0.1)

            # Click inside canvas
            cx = rect.left + (rect.right - rect.left) // 2
            cy = rect.top + (rect.bottom - rect.top) // 2
            print(f"Clicking canvas at ({cx}, {cy})...")
            pyautogui.click(cx, cy)
            time.sleep(0.1)

            print("Pressing F1 via pyautogui and SendInput...")
            for i in range(15):
                pyautogui.press('f1')
                send_scancode(0x3B)
                time.sleep(0.2)

            print("Monitoring post-F1 execution for 30 seconds...")
            for sec in range(1, 31):
                time.sleep(1)
                img = capture_hwnd(hwnd)
                if img:
                    snap_path = OUT_DIR / f"snap_titlefocus_{sec:02d}s.png"
                    img.save(snap_path)
                    print(f"  [+{sec:02d}s] Saved {snap_path.name}")

    finally:
        print("Terminating 86Box...")
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except Exception:
            proc.kill()


if __name__ == "__main__":
    main()
