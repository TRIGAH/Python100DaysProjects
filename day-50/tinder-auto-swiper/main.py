from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException,TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os

FB_EMAIL = "YOUR FACEBOOK LOGIN EMAIL"
FB_PASSWORD = "YOUR FACEBOOK PASSWORD"
chrome_driver_path = "YOUR CHROME DRIVER PATH"

chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("detach", True)
#---------------------------------------------------------------------
#added this argument to retrive chrome data *which my linked credentials already login, to skip CAPTCHA
# chrome_options.add_argument(fr'--profile-directory=Profile 10')
#---------------------------------------------------------------------
chrome_options.add_argument("--start-maximized")
chrome_service = Service(executable_path="C:\Development\chromedriver.exe")
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.get(By.XPATH,'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_button.click()

sleep(2)
fb_login = driver.get(By.XPATH,'//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.get(By.XPATH,'//*[@id="email"]')
password = driver.get(By.XPATH,'//*[@id="pass"]')

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
sleep(5)

#Allow location
allow_location_button = driver.get(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.get(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.get(By.XPATH,'//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()


# wait = WebDriverWait(driver, 10)  # 10 seconds maximum wait time

# try:
#     # Wait for the element to be clickable
#     element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q1946091371"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button/div[2]/div[2]/div')))
    
#     # Interact with the element
#     element.click()
    
# except TimeoutException:
#     print("Element was not clickable within the specified time.")