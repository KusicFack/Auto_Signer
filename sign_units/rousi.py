from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json, os

def rousi_sign(browser, token_file, blank_window, rank, total):
    rank += 1
    print(f"开始签到，第 {rank} 个，共 {total} 个".center(os.get_terminal_size().columns-10, '='))
    print("")
    try:
        print("开始 rousi.pro 签到")
        browser.switch_to.new_window("rouzi")
        browser.get("https://rousi.pro/points")

        print("装载本地 token")
        items = json.load(open(token_file, "r", encoding="utf-8"))
        browser.execute_script("window.localStorage.setItem(\"token\", arguments[0]);", items["token"])

        print("开始签到...")
        browser.get("https://rousi.pro/points")
    except Exception as e:
        print("[错误]：无法访问网站或装载 token，请检查网络或 token 文件是否损坏，以及网站目前是否可用。错误信息如下：\n"+str(e))
        browser.switch_to.window(blank_window)
        print("")
        print(f"签到完成".center(os.get_terminal_size().columns-4, '='))
        print("")
        return rank
    
    try:
        sign_label = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="root"]/div/main/div/div/div[2]/div[3]/div/div''')))
        if not sign_label.find_elements(By.XPATH, "./div[2]"):
            print("[警告]：已经签到过了")
        else:
            sign_label.find_element(By.XPATH, "./div[2]/button[1]").click()
            print("签到成功！")
    except Exception as e:
        print("[错误]：无法签到！请将下列信息提交给开发者\n"+str(e))
    browser.switch_to.window(blank_window)
    print("")
    print(f"签到完成".center(os.get_terminal_size().columns-4, '='))
    print("")
    return rank