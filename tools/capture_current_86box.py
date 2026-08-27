"""Capture screenshot of currently running 86Box window for Gate A."""

import ctypes
from ctypes import wintypes
import time
from pathlib import Path
from PIL import Image

from win32_capture import capture_hwnd

ROOT = Path(__file__).resolve().parent.parent
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
    hwnds = find_86box_window()
    if not hwnds:
        print("No visible 86Box window found. Please ensure 86Box is running.")
        return

    hwnd, title = hwnds[0]
    print(f"Found 86Box window: '{title}' (HWND {hwnd})")
    img = capture_hwnd(hwnd)
    if not img:
        print("Failed to capture window image.")
        return

    full_path = OUT_DIR / "gate-a-startup-full.png"
    img.save(full_path)
    print(f"Saved full window screenshot to {full_path} ({img.size})")

    # If this is the 86Box window with client area, crop the game canvas
    # Window typically has title bar + menu + toolbar + canvas + status bar
    # Client canvas in 640x400 mode is around x: 10..650 or similar
    # Let's also save a closeup
    crop_w, crop_h = img.size
    closeup = img.crop((crop_w // 4, crop_h // 4, crop_w * 3 // 4, crop_h * 3 // 4))
    closeup_path = OUT_DIR / "gate-a-startup-closeup.png"
    closeup.save(closeup_path)
    print(f"Saved closeup to {closeup_path} ({closeup.size})")


if __name__ == "__main__":
    main()
