# A program that navigates to a window with a given title, copied the contents of that window,
# and pastes the contents onto the console.
# This program assumes that the desired window is the first (or only) open window with the given title.

import pyinputplus as pyip, pyautogui, pyperclip


def read_text_field(window_title):
    current_window = pyautogui.getActiveWindow()
    windows = pyautogui.getWindowsWithTitle(window_title)
    if len(windows) == 0:
        print(f'No open windows with title like {window_title}')
    else:
        window = windows[0]
        window.activate()
        pyautogui.moveTo(window.left + 200, window.top + 200)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')

        # Give python a little time to copy the contents successfully
        pyautogui.sleep(1)
        current_window.activate()
        # Printing out the copied contents
        print(pyperclip.paste())


if __name__ == '__main__':
    window_to_read_from = pyip.inputStr(prompt='Please enter the name of the window that you want to copy from:\n')
    read_text_field(window_to_read_from)
