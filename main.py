from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import os

from sign_units.wuai import wuai_sign
from sign_units.rousi import rousi_sign
from sign_units.hifini import hifini_sign
from sign_units.pcbeta import pcbeta_sign

firefox_options = Options() 
firefox_options.add_argument('--headless')
firefox_options.set_preference("general.useragent.override","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0")
firefox_options.add_argument('--width=1920')
firefox_options.add_argument('--height=1080')

# 使用 Termux 时取消下行注释
# firefox_service = Service("/data/data/com.termux/files/usr/bin/geckodriver")

# 使用 Windows 时取消下行注释
firefox_service = Service()

browser = webdriver.Firefox(options=firefox_options, service=firefox_service)
browser.install_addon(os.path.realpath('webdriver-cleaner.xpi'), temporary=True)
browser.install_addon(os.path.realpath('image-blocker.xpi'), temporary=True)
blank_window = browser.current_window_handle

if __name__ == "__main__":
    rank, total = 0, 4
    rank = wuai_sign(browser, "cookies/wuai_cookie.json", blank_window, rank, total)
    rank = rousi_sign(browser, "cookies/rouzi_cookie.json", blank_window, rank, total)
    rank = hifini_sign(browser, "cookies/hifini_cookie.json", blank_window, rank, total)
    rank = pcbeta_sign(browser, "cookies/pcbeta_cookie.json", blank_window, rank, total)
    browser.quit()