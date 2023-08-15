from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
# # EMAIL = os.environ['EMAIL']
# # PASSWORD = os.environ['PASSWORD']

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
driver = webdriver.Chrome(options= chrome_options)
# driver.get("https://www.speedtest.net/")
# wait = WebDriverWait(driver,10)

# go_element = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'))) 
# go_element.click()
# time.sleep(50)

# down_speed = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')))
# print(down_speed.text)

# up_speed = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')))
# print(up_speed.text)

# driver.get("https://twitter.com/i/flow/login")
# username = driver.find_element(By.TAG_NAME,'input')
# username.send_keys("mapstyls")



PROMISED_DOWN = 200
PROMISED_UP = 100
CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"
# TWITTER_EMAIL = os.environ.get("EMAIL")
# TWITTER_PASSWORD = os.environ.get("PASSWORD")
# TWITTER_HANDLE = os.environ.get("TWITTER_HANDLE")


class InternetSpeedTwitterBot:
    """A class for connecting to selenium"""
    def __init__(self):
        self.down = 0
        self.up = 0
        self.chrome_service = Service(executable_path="C:\Development\chromedriver.exe")
        self.driver = webdriver.Chrome(options= chrome_options)
     
    def get_internet_speed(self):
        url = "https://www.speedtest.net/"
        # class start-text
        self.driver.get(url)
        start_test = self.driver.find_element(By.CLASS_NAME, "start-text")
        time.sleep(15)
        start_test.click()
        time.sleep(40)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        print(self.down)
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(self.up)
        time.sleep(5)

    def tweet_at_provider(self):
        url = "https://twitter.com"
        self.driver.get(url)
        time.sleep(5)
        login = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span')
        login.click()
        time.sleep(5)

        # May not need depending upon twitter login format
        twitter_name = self.driver.find_element(By.TAG_NAME, "input")
        twitter_name.send_keys("", Keys.ENTER)
        time.sleep(5)
        password = self.driver.find_elements(By.TAG_NAME, "input")
        password[1].send_keys("", Keys.ENTER)
        time.sleep(10)
        tweet_button = self.driver.find_element(By.LINK_TEXT, "Tweet")
        tweet_button.click()
        time.sleep(5)
        active = self.driver.switch_to.active_element
        active.send_keys(f"Download speed was {self.down} Mps and upload was {self.up} Mps.")
        time.sleep(20)

    def quit(self):
        self.driver.quit()


complaint_bot = InternetSpeedTwitterBot()
complaint_bot.get_internet_speed()
complaint_bot.tweet_at_provider()
complaint_bot.quit()