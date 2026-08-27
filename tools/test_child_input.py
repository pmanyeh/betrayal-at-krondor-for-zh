"""Send F1 and Enter continuously to child video canvas widget."""

import ctypes
from ctypes import wintypes
import subprocess
import time
from pathlib import Path
from PIL import Image

from win32_capture import capture_hwnd
from test_sendinput import send_scancode, send_click, force_foreground

ROOT = Path(__file__).resolve().parent.parent
VM_DIR = ROOT / "scratchpad" / "evg-native-cjk-poc" / "vm"
EXE_86BOX = Path(r"C:\Users\pmany\AppData\Local\Microsoft\WinGet\Packages\86Box.86Box_Microsoft.Winget.Source_8wekyb3d8bbwe\86Box.exe")
OUT_DIR = ROOT / "scratchpad" / "evg-native-cjk-poc"

user32 = ctypes.windll.user32


def get_video_widget(hwnd):
    widgets = []

    def cb(child, lparam):
        rect = wintypes.RECT()
        user32.GetWindowRect(child, ctypes.byref(rect))
        h = rect.bottom - rect.top
        w = rect.right - rect.left
        if h >= 200 and w >= 300:
            widgets.append((child, (rect.left, rect.top, w, h)))
        return True

    EnumChildProc = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
    user32.EnumChildWindows(hwnd, EnumChildProc(cb), 0)
    return widgets[-1] if widgets else (hwnd, None)


def send_key_combo(child_hwnd, vk, scan):
    # PostMessage to child
    user32.PostMessageW(child_hwnd, 0x0100, vk, (scan << 16) | 1)
    time.sleep(0.03)
    user32.PostMessageW(child_hwnd, 0x0101, vk, (scan << 16) | 0xC0000001)

    # SendInput hardware scan code
    send_scancode(scan)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Launching 86Box with VM at {VM_DIR}...")

    # Start 86Box process
    proc = subprocess.Popen([str(EXE_86BOX), "-P", str(VM_DIR)])

    try:
        print("Monitoring 86Box execution for 50 seconds...")
        for sec in range(1, 51):
            time.sleep(1)
            hwnd = user32.FindWindowW(None, "vm - 86Box 6.0 [build 9001]")
            if not hwnd:
                import pyautogui

                wins = pyautogui.getWindowsWithTitle("86Box")
                if wins:
                    hwnd = wins[0]._hWnd

            if hwnd:
                force_foreground(hwnd, proc.pid)
                child_hwnd, rect = get_video_widget(hwnd)

                if sec in range(3, 20):
                    if rect:
                        cx = rect[0] + rect[2] // 2
                        cy = rect[1] + rect[3] // 2
                        send_click(cx, cy)
                    print(f"  [{sec:02d}s] Sending F1 / Enter...")
                    send_key_combo(child_hwnd, 0x70, 0x3B)  # F1
                    time.sleep(0.05)
                    send_key_combo(child_hwnd, 0x0D, 0x1C)  # Enter

                if sec % 2 == 0 or sec >= 8:
                    img = capture_hwnd(hwnd)
                    if img:
                        snap_path = OUT_DIR / f"snap_continuous_{sec:02d}s.png"
                        img.save(snap_path)
                        print(f"  [{sec:02d}s] Saved {snap_path.name}")

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
