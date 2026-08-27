"""Inspect child windows of 86Box while running."""

import ctypes
from ctypes import wintypes
import subprocess
import time
from pathlib import Path

user32 = ctypes.windll.user32

ROOT = Path(__file__).resolve().parent.parent
VM_DIR = ROOT / "scratchpad" / "evg-native-cjk-poc" / "vm"
EXE_86BOX = Path(r"C:\Users\pmany\AppData\Local\Microsoft\WinGet\Packages\86Box.86Box_Microsoft.Winget.Source_8wekyb3d8bbwe\86Box.exe")


def enum_children(hwnd):
    results = []

    def cb(child, lparam):
        cls_buff = ctypes.create_unicode_buffer(256)
        user32.GetClassNameW(child, cls_buff, 256)
        rect = wintypes.RECT()
        user32.GetWindowRect(child, ctypes.byref(rect))
        results.append((child, cls_buff.value, (rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top)))
        return True

    EnumChildProc = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
    user32.EnumChildWindows(hwnd, EnumChildProc(cb), 0)
    return results


def main():
    proc = subprocess.Popen([str(EXE_86BOX), "-P", str(VM_DIR)])
    try:
        time.sleep(4)
        hwnd = user32.FindWindowW(None, "vm - 86Box 6.0 [build 9001]")
        if not hwnd:
            import pyautogui

            w = pyautogui.getWindowsWithTitle("86Box")[0]
            hwnd = w._hWnd

        print(f"Top window: {hwnd}")
        children = enum_children(hwnd)
        for c, cls, r in children:
            print(f"  Child HWND {c}: Class '{cls}', Rect {r}")

    finally:
        proc.terminate()


if __name__ == "__main__":
    main()
