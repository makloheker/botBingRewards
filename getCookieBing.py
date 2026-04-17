import pickle, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.EdgeOptions()
# driver.add_argument("--headless")

browser = webdriver.Edge(options=driver)

browser.get('https://login.live.com/login.srf')


inputUsername = browser.find_element(By.NAME, 'loginfmt')

inputUsername.send_keys("moemoepoi69@gmail.com")

inputUsername.send_keys(Keys.ENTER)


# inputPassword = browser.find_element(By.NAME, "passwd")
inputPassword = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, 'passwd'))
)
inputPassword.send_keys("Yumenosekai@1")
inputPassword.send_keys(Keys.ENTER)

# time.sleep(5)



try:
    inputSubmit = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'iNext')))
    inputSubmit.click()
except:
    print('error next')


try:
    inputStay = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "declineButton")))
    inputStay.click()
except:
    print('error bang')

time.sleep(20)



pageTitle = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "title")))

pageTitle = browser.title
print(pageTitle)
if "Microsoft account | Home" == pageTitle:
    print('berhasil login')
    identity = browser.find_element(By.ID, "meInitialsButton").text
    cookies = browser.get_cookies()
    cookieNameFile = identity+".pkl"
    with open('sessions/'+cookieNameFile, 'wb') as file:
        pickle.dump(cookies, file)
elif "Microsoft account | Account Checkup" == pageTitle:    
    # closeBtn = browser.find_element(By.ID, "landing-page-dialog.close")
    closeBtn = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "landing-page-dialog.close")))
    closeBtn.click()
    # identity = browser.find_element(By.ID, "meInitialsButton").text
    identity = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "meInitialsButton"))).text
    cookies = browser.get_cookies()

    with open('sessions/'+identity+".pkl", 'wb') as file:
        pickle.dump(cookies, file)

time.sleep(999)
browser.quit()
