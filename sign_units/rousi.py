from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json, sys, shutil

def rousi_sign(browser, token_file, blank_window, rank, total, temp_file=sys.stdout):
    rank += 1

    if temp_file is not sys.stdout:
        if rank == 1:
            temp_file=open(temp_file,"wt",encoding="UTF-8")
        else:
            temp_file=open(temp_file,"at",encoding="UTF-8")

    if temp_file is sys.stdout:
        print(f"开始签到，第 {rank} 个，共 {total} 个".center(shutil.get_terminal_size().columns-10, '='), file=temp_file)
    else:
        print(f"开始签到，第 {rank} 个，共 {total} 个".center(shutil.get_terminal_size().columns-8, '='), file=temp_file)
    print("", file=temp_file)

    try:
        print("开始 rousi 签到", file=temp_file)
        browser.switch_to.new_window("rouzi")
        browser.get("https://rousi.pro/points")

        print("装载本地 token", file=temp_file)
        items = json.load(open(token_file, "r", encoding="utf-8"))
        browser.execute_script("window.localStorage.setItem(\"token\", arguments[0]);", items["token"])

        print("开始签到...", file=temp_file)
        browser.get("https://rousi.pro/points")
    except Exception as e:
        print("[错误]：无法访问网站或装载 token，请检查网络或 token 文件是否损坏，以及网站目前是否可用。错误信息如下：\n"+str(e), file=temp_file)
        browser.switch_to.window(blank_window)
        print("", file=temp_file)
        print(f"签到完成".center(shutil.get_terminal_size().columns-4, '='), file=temp_file)
        print("", file=temp_file)
        return rank
    
    try:
        sign_label = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="root"]/div/main/div/div/div[2]/div[3]/div/div''')))
        if not sign_label.find_elements(By.XPATH, "./div[2]"):
            print("[警告]：已经签到过了", file=temp_file)
        else:
            sign_label.find_element(By.XPATH, "./div[2]/button[1]").click()
            print("签到成功！", file=temp_file)
    except Exception as e:
        print("[错误]：无法签到！请将下列信息提交给开发者\n"+str(e), file=temp_file)
    browser.switch_to.window(blank_window)
    print("", file=temp_file)
    print(f"签到完成".center(shutil.get_terminal_size().columns-4, '='), file=temp_file)
    print("", file=temp_file)

    if temp_file is not sys.stdout:
        temp_file.close()
    
    return rank