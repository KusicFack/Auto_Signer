from selenium.webdriver.chromium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.chromium.service import ChromiumService
from pyvirtualdisplay import Display
import os

from sign_units.wuai import wuai_sign
from sign_units.rousi import rousi_sign
from sign_units.hifini import hifini_sign
from sign_units.pcbeta import pcbeta_sign
from sign_units.ablesci import ablesci_sign

display = Display(backend='xvnc')

chromium_options = ChromiumOptions()
chromium_options.add_argument('--no-sandbox')
chromium_options.add_argument('--disable-gpu')
chromium_options.add_argument("--disable-blink-features=AutomationControlled")
chromium_options.add_argument('--disable-webgl')
chromium_options.add_argument('--window-size=1920,1080')
chromium_options.add_extension(os.path.realpath('image-blocker.crx'))

chromium_service = ChromiumService("/data/data/com.termux/files/usr/bin/chromedriver")

if __name__ == "__main__":
    display.start()
    
    browser = webdriver.ChromiumDriver(options=chromium_options, service=chromium_service)
    blank_window = browser.current_window_handle
    
    rank, total = 0, 5
    rank = wuai_sign(browser, "cookies/wuai_cookie.json", blank_window, rank, total)
    rank = rousi_sign(browser, "cookies/rousi_token.json", blank_window, rank, total)
    rank = hifini_sign(browser, "cookies/hifini_cookie.json", blank_window, rank, total)
    rank = pcbeta_sign(browser, "cookies/pcbeta_cookie.json", blank_window, rank, total)
    rank = ablesci_sign(browser, "cookies/ablesci_cookie.json", blank_window, rank, total)
    browser.quit()
    
    display.stop()