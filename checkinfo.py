import pickle, time, json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


def checkBotInfo(kuki):
    
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
    options = webdriver.EdgeOptions()
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--guest")
    options = webdriver.EdgeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    options.add_argument("--log-level=3")
    options.add_argument("--headless")
    options.add_argument("start-maximized")
    driver = webdriver.Edge(options=options)

    driver.get("https://rewards.bing.com/favicon.ico")
    time.sleep(1)
    with open("cookie/rewards/"+kuki, "r") as f:
        cookies = json.load(f)
    for cookie in cookies:
        cookie.pop("sameSite", None) 
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"Gagal menambahkan cookie {cookie.get('name')}: {e}")
    driver.refresh()
    driver.get("https://rewards.bing.com/pointsbreakdown")
    time.sleep(2)
    points = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".pointsDetail.c-subheading-3.ng-binding"))
    )


    # texts = [p.text for p in points]
    # print("Points: " + " | ".join(texts))
    print("===============================")
    print("Account : "+kuki)
    print("Desktop : "+points[0].text)
    print("Mobile  : "+points[1].text)
    print("===============================")




def checkMission(kuki):
    
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
    options = webdriver.EdgeOptions()
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--guest")


    options = webdriver.EdgeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    options.add_argument("--log-level=3")
    # options.add_argument("--headless")
    options.add_argument("start-maximized")
    driver = webdriver.Edge(options=options)

    driver.get("https://rewards.bing.com/favicon.ico")
    time.sleep(1)
    with open("cookie/rewards/"+kuki, "r") as f:
        cookies = json.load(f)
    for cookie in cookies:
        cookie.pop("sameSite", None) 
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"Gagal menambahkan cookie {cookie.get('name')}: {e}")
    driver.refresh()
    driver.get("https://rewards.bing.com/")
    # time.sleep(2)
    # dailys = WebDriverWait(driver, 15).until(
    #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "mee-card-group a"))
    # )
    # main_tab = driver.current_window_handle

    # for link in dailys:
    #     url = link.get_attribute("href")
    
    #     if url != "https://rewards.bing.com/#":
    #         link.click()
    #         all_tabs = driver.window_handles
    #         new_tab = [t for t in all_tabs if t != main_tab][0]
    #         driver.switch_to.window(new_tab)
    #         WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    #         print("Title tab baru:", driver.title)
    #         time.sleep(20)
    #         # elements = driver.find_elements(By.ID, "b_results")
    #         # body = driver.find_element(By.TAG_NAME, "body")
    #         # time.sleep(1)
    #         # if elements:
    #         #     continue
    #         # else:
    #         #     time.sleep(10)
    #         #     for i in range(1, 12):
    #         #         body.send_keys(Keys.TAB)
    #         #         time.sleep(0.5)
    #         #     time.sleep(1)
    #         #     pyautogui.press("space")                
    #         #     time.sleep(5)
    #         driver.close()
    #         driver.switch_to.window(main_tab)
    time.sleep(99999)
    
