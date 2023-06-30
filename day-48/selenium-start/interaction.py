from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
browser.get("http://secure-retreat-92358.herokuapp.com/")
# number_of_articles=browser.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]')
# print(number_of_articles.text)

# search = browser.find_element(By.NAME,"search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

first_name = browser.find_element(By.NAME,"fName")
first_name.send_keys("Maps")

last_name = browser.find_element(By.NAME,"lName")
last_name.send_keys("Ijen")

email = browser.find_element(By.NAME,"email")
email.send_keys("maps@gking.com")

sign_up = browser.find_element(By.TAG_NAME,"button")
sign_up.click()
