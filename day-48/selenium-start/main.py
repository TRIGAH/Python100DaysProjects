from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# product_url = "https://www.amazon.com/dp/B099K1QJ2Q/ref=syn_sd_onsite_desktop_0?ie=UTF8&psc=1&pf_rd_p=0c4daa46-238c-491d-9522-631142ac3b5a&pf_rd_r=9NR6XJPNP7CD9KS54A2D&pd_rd_wg=ntCYX&pd_rd_w=fNvc9&pd_rd_r=25c9d67a-1e35-405d-886d-98212dea3081"
chrome_driver_path = "C:\Development\chromedriver.exe"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
# browser.get(product_url)
# price=browser.find_element(By.CLASS_NAME,"a-price")
# print(price.text)
# browser.close()


url ="https://www.python.org/"
browser.get(url)
upcoming_events = {}

times = browser.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
names = browser.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')

for x in range(len(times)):
    upcoming_events[x]={
        "time":times[x].text,
        "name":names[x].text
    }
print(upcoming_events)
browser.close()