# A program that uses selenium to play the 2048 game

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as Exceptions, time


def play_2048():
    browser = webdriver.Chrome()
    browser.get('https://gabrielecirulli.github.io/2048/')

    while True:
        try:
            html_elem = browser.find_element_by_tag_name('html')
            html_elem.send_keys(Keys.UP)
            html_elem.send_keys(Keys.RIGHT)
            html_elem.send_keys(Keys.DOWN)
            html_elem.send_keys(Keys.LEFT)
            game_over = browser.find_element_by_css_selector(
                'body > div.container > div.game-container > div.game-message.game-over')
            if game_over is not None:
                break
        except Exceptions.NoSuchElementException:
            continue
        except Exceptions.WebDriverException as e:
            continue

    # Display the results on the screen
    time.sleep(10)
    browser.close()


if __name__ == '__main__':
    play_2048()
