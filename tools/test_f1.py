"""Test activating 86Box window with Alt bypass and pressing F1."""

import ctypes
from ctypes import wintypes
import subprocess
import time
from pathlib import Path
import pyautogui
from PIL import Image

from win32_capture import capture_hwnd

pyautogui.FAILSAFE = False

ROOT = Path(__file__).resolve().parent.parent
VM_DIR = ROOT / "scratchpad" / "evg-native-cjk-poc" / "vm"
EXE_86BOX = Path(r"C:\Users\pmany\AppData\Local\Microsoft\WinGet\Packages\86Box.86Box_Microsoft.Winget.Source_8wekyb3d8bbwe\86Box.exe")
OUT_DIR = ROOT / "scratchpad" / "evg-native-cjk-poc"

user32 = ctypes.windll.user32


def force_foreground(hwnd, pid):
    user32.AllowSetForegroundWindow(pid)
    user32.keybd_event(0x12, 0, 0, 0)  # Alt down
    time.sleep(0.02)
    user32.ShowWindow(hwnd, 9)
    user32.SetForegroundWindow(hwnd)
    user32.SetFocus(hwnd)
    time.sleep(0.02)
    user32.keybd_event(0x12, 0, 2, 0)  # Alt up


def main():
    proc = subprocess.Popen([str(EXE_86BOX), "-P", str(VM_DIR)])
    try:
        print("Waiting 6 seconds for 86Box to boot to F1 prompt...")
        time.sleep(6)

        wins = pyautogui.getWindowsWithTitle("86Box")
        if wins:
            w = wins[0]
            hwnd = w._hWnd
            print(f"Found window: {w.title} (HWND: {hwnd})")

            force_foreground(hwnd, proc.pid)
            time.sleep(0.5)

            # Click firmly in the center
            rect = wintypes.RECT()
            user32.GetWindowRect(hwnd, ctypes.byref(rect))
            cx = (rect.left + rect.right) // 2
            cy = (rect.top + rect.bottom) // 2
            print(f"Clicking at ({cx}, {cy})...")
            user32.SetCursorPos(cx, cy)
            time.sleep(0.05)
            pyautogui.click(cx, cy)
            time.sleep(0.2)

            print("Pressing F1 multiple times...")
            for i in range(5):
                pyautogui.press('f1')
                time.sleep(0.3)

            print("Monitoring post-F1 execution for 20 seconds...")
            for sec in range(1, 21):
                time.sleep(1)
                img = capture_hwnd(hwnd)
                if img:
                    snap_path = OUT_DIR / f"snap_f1_{sec:02d}s.png"
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
