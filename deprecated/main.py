from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from pyvirtualdisplay import Display
import os

from sign_units.wuai import wuai_sign
from sign_units.rousi import rousi_sign
from sign_units.hifini import hifini_sign
from sign_units.pcbeta import pcbeta_sign

display = Display(backend='xvfb')

firefox_options = FirefoxOptions()
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-gpu')
firefox_options.add_argument('--width=1920')
firefox_options.add_argument('--height=1080')
firefox_options.set_preference("webgl.disabled", True)
# firefox_options.binary_location = ""

# 使用 Termux 时取消下行注释
# firefox_service = FirefoxService("/data/data/com.termux/files/usr/bin/geckodriver")

# 使用 Windows 时取消下行注释
# firefox_service = FirefoxService()

if __name__ == "__main__":
    # display.start()

    browser = webdriver.Firefox(options=firefox_options, service=firefox_service)
    blank_window = browser.current_window_handle

    browser.install_addon(os.path.realpath('webdriver-cleaner.xpi'), temporary=True)
    browser.install_addon(os.path.realpath('image-blocker.xpi'), temporary=True)

    rank, total = 0, 4
    rank = wuai_sign(browser, "cookies/wuai_cookie.json", blank_window, rank, total)
    rank = rousi_sign(browser, "cookies/rouzi_cookie.json", blank_window, rank, total)
    rank = hifini_sign(browser, "cookies/hifini_cookie.json", blank_window, rank, total)
    rank = pcbeta_sign(browser, "cookies/pcbeta_cookie.json", blank_window, rank, total)
    browser.quit()

    # display.stop()