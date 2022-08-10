import time
import keyboard
import win32api
import win32con
import win32gui


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


cooldown = 0
upgrade = 1000
r = 1  # ensures the window doesn't close after the first increment


print("Welcome to Cookie Clicker Bot v2! - Created 10/07/2022")
print("The bot will click for cookies and regularly check for upgrades.")
print("This window will automatically close on start. \n")
print("Press 'R' to run.")
print("Press 'P' to pause.")
print("Press 'Q' to quit.")


while True:
    if keyboard.is_pressed('q'):
        quit()
    if keyboard.is_pressed('r'):
        if r == 1:
            hide = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(hide, win32con.SW_HIDE)
            r += 1
        if r > 1:
            while not keyboard.is_pressed('p'):
                if keyboard.is_pressed('q'):
                    quit()
                if cooldown < 300:
                    click(151, 426)
                    cooldown += 1
                elif cooldown == 300:
                    click(675, 119)
                    cooldown += 1
                elif upgrade > 200:
                    click(675, upgrade)
                    upgrade -= 60
                else:
                    cooldown = 0
                    upgrade = 1000
