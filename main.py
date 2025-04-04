from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json,os

firefox_options = Options() 
firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')
firefox_options.add_argument("--User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0")
firefox_options.set_preference('permissions.default.image',2)
firefox_options.add_argument('--window-size=1920,1080')

# firefox_service = Service("/data/data/com.termux/files/usr/bin/geckodriver")
firefox_service = Service()

browser = webdriver.Firefox(options=firefox_options, service=firefox_service)
browser.install_addon(os.path.realpath('webdriver-cleaner.xpi'), temporary=True)
blank_window = browser.current_window_handle


def info_decorator(func):
    def wrapper(*args, **kwargs):
        global rank, total
        rank += 1
        print(f"开始签到，第 {rank} 个，共 {total} 个".center(40, '='))
        print("")
        result = func(*args, **kwargs)
        print("")
        print(f"签到完成".center(46, '='))
        print("")
        return result
    return wrapper

@info_decorator
def wuai_sign(browser, cookie_file):
    try:
        print("开始 吾爱破解 签到")
        browser.switch_to.new_window("wuai")
        browser.get("https://www.52pojie.cn/home.php?mod=task&do=view&id=2")

        print("清除预设 cookies")
        browser.delete_all_cookies()
        
        print("装载本地 cookies")
        cookies = json.load(open(cookie_file, "r", encoding="utf-8"))
        for cookie in cookies:
            browser.add_cookie(cookie)

        print("开始签到...")
        browser.refresh()
    except Exception as e:
        print("[错误]：无法访问网站或装载 cookies，请检查网络或 cookies 文件是否损坏，以及网站目前是否可用。错误信息如下：\n"+str(e))
        browser.delete_all_cookies()
        browser.close()
        browser.switch_to.window(blank_window)
        return
    
    try:
        locator = (By.XPATH, '''//div[@id="ct"]/div[1]/div/div/table/tbody/tr[3]/td[2]/a[@href="javascript:;"]''')
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(locator)
        )
        with open("wuai.html", "w", encoding="utf-8") as f:
            f.write(browser.page_source)
        sign_label = browser.find_element(by=By.XPATH, value='''//div[@id="ct"]/div[1]/div/div/table/tbody/tr[3]/td[2]/a[@href="javascript:;"]''')
        if "再次申请" in sign_label.get_attribute("onclick").strip():
            print("[警告]：已经签到过了")
        else:
            sign_label.click()
            print("签到成功！更新本地 cookies")
            cookies = browser.get_cookies()
            json.dump(cookies, open(cookie_file, "w", encoding="utf-8"), ensure_ascii=False, indent=4)
    except Exception as e:
        print("[错误]：无法签到！请将下列信息提交给开发者\n"+str(e))
    
    browser.delete_all_cookies()
    browser.close()
    browser.switch_to.window(blank_window)

@info_decorator 
def rousi_sign(browser, cookie_file):
    try:
        print("开始 rouzi.zip 签到")
        browser.switch_to.new_window("rouzi")
        browser.get("https://rousi.zip/index.php")

        print("清除预设 cookies")
        browser.delete_all_cookies()
        
        print("装载本地 cookies")
        cookies = json.load(open(cookie_file, "r", encoding="utf-8"))
        for cookie in cookies:
            browser.add_cookie(cookie)

        print("开始签到...")
        browser.refresh()
    except Exception as e:
        print("[错误]：无法访问网站或装载 cookies，请检查网络或 cookies 文件是否损坏，以及网站目前是否可用。错误信息如下：\n"+str(e))
        browser.delete_all_cookies()
        browser.close()
        browser.switch_to.window(blank_window)
        return
    
    try:
        sign_label = browser.find_element(by=By.XPATH, value='''//*[@id="info_block"]/tbody/tr/td/table/tbody/tr/td[1]/span/a[5]''')
        if not sign_label.get_attribute("class"):
            print("[警告]：已经签到过了")
        else:
            sign_label.click()
            print("签到成功！更新本地 cookies")
            cookies = browser.get_cookies()
            json.dump(cookies, open(cookie_file, "w", encoding="utf-8"), ensure_ascii=False, indent=4)
    except Exception as e:
        print("[错误]：无法签到！请将下列信息提交给开发者\n"+str(e))
    
    browser.delete_all_cookies()
    browser.close()
    browser.switch_to.window(blank_window)

@info_decorator
def hifini_sign(browser, cookie_file):
    try:
        print("开始 hifini 签到")
        browser.switch_to.new_window("hifini")
        browser.get("https://www.hifini.com/")

        print("清除预设 cookies")
        browser.delete_all_cookies()
        
        print("装载本地 cookies")
        cookies = json.load(open(cookie_file, "r", encoding="utf-8"))
        for cookie in cookies:
            browser.add_cookie(cookie)

        print("开始签到...")
        browser.refresh()
    except Exception as e:
        print("[错误]：无法访问网站或装载 cookies，请检查网络或 cookies 文件是否损坏，以及网站目前是否可用。错误信息如下：\n"+str(e))
        browser.delete_all_cookies()
        browser.close()
        browser.switch_to.window(blank_window)
        return
    
    try:
        sign_label = browser.find_element(by=By.XPATH, value='''//div[@id="sign"]''')
        if sign_label.text.strip() == "已签":
            print("[警告]：已经签到过了")
        else:
            sign_label.click()
            print("签到成功！更新本地 cookies")
            cookies = browser.get_cookies()
            json.dump(cookies, open(cookie_file, "w", encoding="utf-8"), ensure_ascii=False, indent=4)
    except Exception as e:
        print("[错误]：无法签到！请将下列信息提交给开发者\n"+str(e))
    
    browser.delete_all_cookies()
    browser.close()
    browser.switch_to.window(blank_window)

@info_decorator
def pcbeta_sign(browser, cookie_file):
    try:
        print("开始 远景论坛 签到")
        browser.switch_to.new_window("pcbeta")
        browser.get("https://i.pcbeta.com/home.php?mod=task&do=view&id=149")

        print("清除预设 cookies")
        browser.delete_all_cookies()
        
        print("装载本地 cookies")
        cookies = json.load(open(cookie_file, "r", encoding="utf-8"))
        for cookie in cookies:
            browser.add_cookie(cookie)

        print("开始签到...")
        browser.refresh()
    except Exception as e:
        print("[错误]：无法访问网站或装载 cookies，请检查网络或 cookies 文件是否损坏，以及网站目前是否可用。错误信息如下：\n"+str(e))
        browser.delete_all_cookies()
        browser.close()
        browser.switch_to.window(blank_window)
        return
    
    try:
        sign_label = browser.find_element(by=By.XPATH, value='''//*[@id="ct"]/div[1]/div/div/table/tbody/tr[3]/td[2]/a''')
        if "再次申请" in sign_label.get_attribute("title").strip():
            print("[警告]：已经签到过了")
        else:
            sign_label.click()
            print("签到成功！更新本地 cookies")
            cookies = browser.get_cookies()
            json.dump(cookies, open(cookie_file, "w", encoding="utf-8"), ensure_ascii=False, indent=4)
    except Exception as e:
        print("[错误]：无法签到！请将下列信息提交给开发者\n"+str(e))
    
    browser.delete_all_cookies()
    browser.close()
    browser.switch_to.window(blank_window)

if __name__ == "__main__":
    rank, total = 0, 4
    wuai_sign(browser, "cookies/wuai_cookie.json")
    # rousi_sign(browser, "cookies/rouzi_cookie.json")
    # hifini_sign(browser, "cookies/hifini_cookie.json")
    # pcbeta_sign(browser, "cookies/pcbeta_cookie.json")
    browser.quit()