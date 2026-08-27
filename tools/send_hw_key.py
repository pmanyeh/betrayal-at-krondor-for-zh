"""Send hardware scancode using keybd_event with KEYEVENTF_SCANCODE."""

import ctypes
from ctypes import wintypes
import time

user32 = ctypes.windll.user32

KEYEVENTF_SCANCODE = 0x0008
KEYEVENTF_KEYUP = 0x0002
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004


def send_hardware_f1(hwnd):
    # Bring window to foreground
    user32.ShowWindow(hwnd, 9)
    user32.SetForegroundWindow(hwnd)
    time.sleep(0.05)

    # Click in the middle of client area
    rect = wintypes.RECT()
    user32.GetClientRect(hwnd, ctypes.byref(rect))
    pt = wintypes.POINT((rect.right - rect.left) // 2, (rect.bottom - rect.top) // 2)
    user32.ClientToScreen(hwnd, ctypes.byref(pt))

    # Move and click
    user32.SetCursorPos(pt.x, pt.y)
    user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.02)
    user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(0.05)

    # Send F1 with SCANCODE (0x3B)
    user32.keybd_event(0, 0x3B, KEYEVENTF_SCANCODE, 0)
    time.sleep(0.08)
    user32.keybd_event(0, 0x3B, KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP, 0)
    time.sleep(0.05)

    # Send Enter with SCANCODE (0x1C)
    user32.keybd_event(0, 0x1C, KEYEVENTF_SCANCODE, 0)
    time.sleep(0.08)
    user32.keybd_event(0, 0x1C, KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP, 0)
