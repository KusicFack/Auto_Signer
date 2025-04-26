from selenium.webdriver.chromium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.chromium.service import ChromiumService
import os

from sign_units.rousi import rousi_sign
from sign_units.hifini import hifini_sign
from sign_units.pcbeta import pcbeta_sign

chromium_options = ChromiumOptions() 
chromium_options.add_argument('--headless=new')
chromium_options.add_argument('--no-sandbox')
chromium_options.add_argument('--disable-gpu')
chromium_options.add_argument("--disable-blink-features=AutomationControlled")

# 根据平台选择合适的 User-Agent
# chromium_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0")
# chromium_options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36")

chromium_options.add_argument('--window-size=1920,1080')
chromium_options.add_extension(os.path.realpath('image-blocker.crx'))

# 使用 Termux 时取消下行注释
# chromium_service = ChromiumService("/data/data/com.termux/files/usr/bin/chromedriver")

# 使用 Windows 时取消下行注释（需自行添加 chromedriver 以及 chromium 文件位置）
# chromium_service = ChromiumService()
# chromium_options.binary_location = ""

browser = webdriver.ChromiumDriver(options=chromium_options, service=chromium_service)
blank_window = browser.current_window_handle

if __name__ == "__main__":
    rank, total = 0, 3
    rank = rousi_sign(browser, "cookies/rouzi_cookie.json", blank_window, rank, total)
    rank = hifini_sign(browser, "cookies/hifini_cookie.json", blank_window, rank, total)
    rank = pcbeta_sign(browser, "cookies/pcbeta_cookie.json", blank_window, rank, total)
    browser.quit()