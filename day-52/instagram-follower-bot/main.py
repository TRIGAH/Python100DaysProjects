from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
import time

chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = "barr_chef"
PASSWORD = "#b@rrchef1$"


class InstaFollower:

    def __init__(self, path):
        self.chrome_service =  Service(executable_path=path)
        self.driver = webdriver.Chrome(options= chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element(By.TAG_NAME,'ul')
        print(followers)

        # time.sleep(2)
        # modal = self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_JA"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div')
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR,"div button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_JA"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button/div/svg/line')
                cancel_button.click()


bot = InstaFollower("C:\Development\chromedriver.exe")
bot.login()
bot.find_followers()
bot.follow()
