from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
browser.get("http://orteil.dashnet.org/experiments/cookie/")
timeout = 60  # [seconds]
timeout_start = time.time()

while time.time() < timeout_start + timeout:
    test = 0
    if test == 5:
        break
    time.sleep(1)
    cookie_maker = browser.find_element(By.ID,'cookie')
    cookie_maker.click()

    cookie_store = browser.find_element(By.CSS_SELECTOR,"#store")

    cookies_made = browser.find_element(By.CSS_SELECTOR,"#money")
    money = int(cookies_made.text)
    print(money)

    cursor = browser.find_element(By.CSS_SELECTOR,"#buyCursor")
    cursor_cost = int(cursor.text.split('\n')[0].split('-')[1].strip())
    print(cursor_cost)

    grandma = browser.find_element(By.CSS_SELECTOR,'#buyGrandma')
    grandma_cost = int(grandma.text.split('\n')[0].split('-')[1].strip())
    print(grandma_cost)

    if money == cursor_cost:
        cursor.click()
    elif money == grandma_cost:
        grandma.click()    
    elif money > cursor_cost and money >= grandma_cost:
        grandma.click()   


cookies_per_second = browser.find_element(By.ID,"cps")
print(cookies_per_second.text)        