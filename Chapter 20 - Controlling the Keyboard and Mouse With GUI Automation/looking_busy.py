# A program that moves the mouse cursor slightly every 10 seconds.

import pyautogui


def looking_busy():
    print('Looking busy. Press Ctrl-C to quit')
    try:
        while True:
            pyautogui.move(3, 3, 0.5)
            pyautogui.move(-3, -3, 0.5)
            pyautogui.sleep(1)
    except KeyboardInterrupt:
        print('No longer looking busy. Exiting program.')


if __name__ == '__main__':
    looking_busy()
