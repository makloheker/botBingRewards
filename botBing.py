import json
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import ai, random, time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style, init
import os


def startBot(kuki, mode, jumlah):
    user_mode = mode
    jumlahSearch = jumlah
    if user_mode == "desktop":
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
        tabstabs = 13
    elif user_mode == "mobile":
        user_agent = "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.3519.0 Mobile Safari/537.36 EdgA/141.0.3519.0"
        tabstabs = 8
    print(user_mode)
    options = webdriver.EdgeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--guest")
    options.add_argument("--window-size=800,800")

    driver = webdriver.Edge(options=options)

    actions = ActionChains(driver)

    def smooth_mouse_wiggle(actions, steps=10, max_offset=40, delay=0.01):
        for _ in range(steps):
            x_offset = random.randint(-max_offset, max_offset)
            y_offset = random.randint(-max_offset, max_offset)
            try:
                actions.move_by_offset(x_offset, y_offset).perform()
            except Exception:
                body = driver.find_element("tag name", "body")
                actions.move_to_element_with_offset(body, 200, 200).perform()
            time.sleep(delay)

    # --- Fungsi: Scroll dengan batas waktu ---
    def smooth_scroll_with_mouse(driver, actions, duration=30, step_range=(30, 80), delay_range=(0.02, 0.06)):
        """
        Scroll halus + gerak mouse, tapi berhenti setelah 'duration' detik
        """
        start_time = time.time()

        while True:
            # stop kalau sudah lewat waktu
            if time.time() - start_time > duration:
                print("⏰ Waktu habis, stop scroll.")
                break

            # Scroll step random
            step = random.randint(*step_range)
            driver.execute_script(f"window.scrollBy(0, {step});")

            # Gerak kursor
            smooth_mouse_wiggle(actions, steps=random.randint(5, 15))

            # Delay acak
            time.sleep(random.uniform(*delay_range))


    driver.get("https://www.bing.com/search")
    time.sleep(2)
    # Load cookie dari file
    with open("cookie/"+mode+"/"+kuki, "r") as f:
        cookies = json.load(f)

    for cookie in cookies:
        cookie.pop("sameSite", None)  # hapus key yang ga didukung
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"Gagal menambahkan cookie {cookie.get('name')}: {e}")

    # Refresh agar cookie aktif
    driver.refresh()
    time.sleep(3)
    driver.refresh()
    print("-----------------------")
    print(f"cookie : {kuki}")
    print("-----------------------")
    time.sleep(2)
    list_pencarian = ai.generate(jumlahSearch)
    while any(val == "" for val in list_pencarian):
        print("Ditemukan string kosong, generate ulang...")
        list_pencarian = ai.generate(jumlahSearch)
    print(list_pencarian)
    for list in list_pencarian:
        time.sleep(7)
        search_box = driver.find_element(By.ID,'sb_form_q')
        search_box.send_keys(Keys.CONTROL + 'a')
        search_box.send_keys(Keys.BACKSPACE)
        search_box.send_keys(list)
        time.sleep(3)
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)
        elements = driver.find_elements(By.ID, "b_results")
        body = driver.find_element("tag name", "body")
        if elements:
            time.sleep(5)
            smooth_scroll_with_mouse(driver, actions, duration=5)
            if user_mode == "mobile":
                driver.refresh()
                time.sleep(2)
                hamButton = driver.find_element(By.ID, "mHamburger")
                hamButton.click()
                time.sleep(5)
                driver.refresh()
        else:
            time.sleep(15)
            for i in range(1, tabstabs):  # 7 mobile 12 desktop
                body.send_keys(Keys.TAB)
                time.sleep(0.5)
            time.sleep(1)
            pyautogui.press("space")                
            time.sleep(5)
    driver.delete_all_cookies()
    driver.quit()



