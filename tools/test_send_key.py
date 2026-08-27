"""AttachThreadInput and send key to 86Box window."""

import ctypes
from ctypes import wintypes
import time

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

VK_F1 = 0x70
KEYEVENTF_KEYUP = 0x0002


def send_key_to_hwnd(hwnd, vk_code, scan_code):
    current_thread = kernel32.GetCurrentThreadId()
    target_thread = user32.GetWindowThreadProcessId(hwnd, None)

    # Attach input
    user32.AttachThreadInput(current_thread, target_thread, True)

    # Restore and foreground
    user32.ShowWindow(hwnd, 9)  # SW_RESTORE
    user32.SetForegroundWindow(hwnd)
    user32.SetFocus(hwnd)
    time.sleep(0.05)

    # keybd_event with scan code
    user32.keybd_event(vk_code, scan_code, 0, 0)
    time.sleep(0.05)
    user32.keybd_event(vk_code, scan_code, KEYEVENTF_KEYUP, 0)

    # Detach
    user32.AttachThreadInput(current_thread, target_thread, False)
