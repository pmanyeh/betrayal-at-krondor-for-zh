"""Test SendInput with hardware scancodes."""

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


class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", wintypes.WORD),
        ("wScan", wintypes.WORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.c_ulong),
    ]


class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.c_ulong),
    ]


class INPUT_UNION(ctypes.Union):
    _fields_ = [("ki", KEYBDINPUT), ("mi", MOUSEINPUT)]


class INPUT(ctypes.Structure):
    _fields_ = [("type", wintypes.DWORD), ("u", INPUT_UNION)]


def send_scancode(scan, is_ext=False):
    flags_down = 0x0008 | (0x0001 if is_ext else 0)
    flags_up = 0x0008 | 0x0002 | (0x0001 if is_ext else 0)

    inp_down = INPUT(1)
    inp_down.u.ki = KEYBDINPUT(0, scan, flags_down, 0, 0)

    inp_up = INPUT(1)
    inp_up.u.ki = KEYBDINPUT(0, scan, flags_up, 0, 0)

    user32.SendInput(1, ctypes.byref(inp_down), ctypes.sizeof(INPUT))
    time.sleep(0.08)
    user32.SendInput(1, ctypes.byref(inp_up), ctypes.sizeof(INPUT))
    time.sleep(0.05)


def send_click(x, y):
    user32.SetCursorPos(x, y)
    time.sleep(0.02)
    inp_down = INPUT(0)
    inp_down.u.mi = MOUSEINPUT(0, 0, 0, 0x0002, 0, 0)  # LEFTDOWN
    inp_up = INPUT(0)
    inp_up.u.mi = MOUSEINPUT(0, 0, 0, 0x0004, 0, 0)  # LEFTUP
    user32.SendInput(1, ctypes.byref(inp_down), ctypes.sizeof(INPUT))
    time.sleep(0.02)
    user32.SendInput(1, ctypes.byref(inp_up), ctypes.sizeof(INPUT))
    time.sleep(0.05)


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

        hwnd = user32.FindWindowW(None, "vm - 86Box 6.0 [build 9001]")
        if not hwnd:
            # Fallback
            import pyautogui
            wins = pyautogui.getWindowsWithTitle("86Box")
            if wins:
                hwnd = wins[0]._hWnd

        if hwnd:
            print(f"Target HWND: {hwnd}")
            force_foreground(hwnd, proc.pid)
            time.sleep(0.3)

            rect = wintypes.RECT()
            user32.GetWindowRect(hwnd, ctypes.byref(rect))
            cx = rect.left + (rect.right - rect.left) // 2
            cy = rect.top + (rect.bottom - rect.top) // 2
            print(f"Clicking at ({cx}, {cy})...")
            send_click(cx, cy)
            time.sleep(0.2)

            print("Sending hardware F1 scancode (0x3B)...")
            for _ in range(5):
                send_scancode(0x3B)  # F1
                time.sleep(0.2)

            print("Monitoring post-F1 execution for 20 seconds...")
            for sec in range(1, 21):
                time.sleep(1)
                img = capture_hwnd(hwnd)
                if img:
                    snap_path = OUT_DIR / f"snap_sendinput_{sec:02d}s.png"
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
