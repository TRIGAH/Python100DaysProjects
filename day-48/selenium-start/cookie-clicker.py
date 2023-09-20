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
timeout = 300  # [seconds]
timeout_start = time.time()

cookies_made = browser.find_element(By.CSS_SELECTOR,"#money")
money = int(cookies_made.text)

cookie_store = browser.find_elements(By.CSS_SELECTOR,"#store div")
items = [ item.get_attribute("id") for item in cookie_store]
cookie_store_dict = {}

while time.time() < timeout_start + timeout:
    time.sleep(1)
    cookie_maker = browser.find_element(By.ID,'cookie')
    cookie_maker.click()

    for item in items:
        item_cost = browser.find_element(By.ID,item)
        if item_cost.text != '':
            cookie_store_dict[item] = item_cost.text.split('\n')[0].split('-')[1].strip().replace(',','')
        else:
            pass  

    for item,price in cookie_store_dict.items():
        if money == int(cookie_store_dict[item]):
            upgrade = browser.find_element(By.ID,item)
            upgrade.click()
    
cookies_per_second = browser.find_element(By.ID,"cps")
print(cookies_per_second.text)    





    