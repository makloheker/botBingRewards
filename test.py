import json
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import ai, random, time
from selenium.webdriver.common.action_chains import ActionChains
from colorama import Fore, Style, init
import os




def startBotNormal(kuki, mode):
    user_mode = mode
    if user_mode == "desktop":
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"        
    elif user_mode == "mobile":
        user_agent = "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.3519.0 Mobile Safari/537.36 EdgA/141.0.3519.0"
    options = webdriver.EdgeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--guest")
    options.add_argument("--window-size=800,800")

    driver = webdriver.Edge(options=options)


    driver.get("https://rewards.bing.com/favicon.ico")
    time.sleep(2)
    with open("cookie/reward/"+kuki, "r") as f:
        cookies = json.load(f)

    for cookie in cookies:
        cookie.pop("sameSite", None) 
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"Gagal menambahkan cookie {cookie.get('name')}: {e}")

    driver.refresh()
    driver.get("https://rewards.bing.com/")
    print("-----------------------")
    print(f"cookie : {kuki}")
    print("-----------------------")
    time.sleep(99999)

if __name__ == "__main__":
    startBotNormal("cookie.json", "desktop")