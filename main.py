import pyautogui
import win32api
import win32con
import time

time.sleep(5)

while True:
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    pyautogui.moveTo(center_x, center_y)
    pyautogui.click(button='right')
    win32api.SetCursorPos((center_x, center_y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

    image_path = 'data/image.png'

    time.sleep(1)

    image_location = pyautogui.locateOnScreen(image_path, confidence=0.8)

    if image_location is not None:
        image_center = pyautogui.center(image_location)
        pyautogui.moveTo(image_center)
        pyautogui.click(button='right')
        win32api.SetCursorPos((image_center.x, image_center.y))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

    else:
        print("Failed ")

    time.sleep(15)
