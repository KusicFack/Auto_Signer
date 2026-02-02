from selenium.webdriver.common.by import By
import json, sys, shutil

def pcbeta_sign(browser, cookie_file, blank_window, rank, total, temp_file=sys.stdout):
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
        print("开始 远景论坛 签到", file=temp_file)
        browser.switch_to.new_window("pcbeta")
        browser.get("https://i.pcbeta.com/home.php?mod=task&do=view&id=149")

        print("清除预设 cookies", file=temp_file)
        browser.delete_all_cookies()
        
        print("装载本地 cookies", file=temp_file)
        cookies = json.load(open(cookie_file, "r", encoding="utf-8"))
        for cookie in cookies:
            browser.add_cookie(cookie)

        print("开始签到...", file=temp_file)
        browser.refresh()
    except Exception as e:
        print("[错误]：无法访问网站或装载 cookies，请检查网络或 cookies 文件是否损坏，以及网站目前是否可用。错误信息如下：\n"+str(e), file=temp_file)
        browser.switch_to.window(blank_window)
        print("", file=temp_file)
        print(f"签到完成".center(shutil.get_terminal_size().columns-4, '='), file=temp_file)
        print("", file=temp_file)
        return rank
    
    try:
        sign_label = browser.find_element(by=By.XPATH, value='''//*[@id="ct"]/div[1]/div/div/table/tbody/tr[3]/td[2]/a''')
        if "再次申请" in sign_label.get_attribute("title").strip():
            print("[警告]：已经签到过了", file=temp_file)
        else:
            sign_label.click()
            print("签到成功！更新本地 cookies", file=temp_file)
            cookies = browser.get_cookies()
            json.dump(cookies, open(cookie_file, "w", encoding="utf-8"), ensure_ascii=False, indent=4)
    except Exception as e:
        print("[错误]：无法签到！请将下列信息提交给开发者\n"+str(e), file=temp_file)

    browser.switch_to.window(blank_window)
    print("", file=temp_file)
    print(f"签到完成".center(shutil.get_terminal_size().columns-4, '='), file=temp_file)
    print("", file=temp_file)

    if temp_file is not sys.stdout:
        temp_file.close()
    
    return rank