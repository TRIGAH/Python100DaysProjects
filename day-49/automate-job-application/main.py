# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import ElementClickInterceptedException
# from selenium.webdriver.support.ui import WebDriverWait

# import time

# chrome_driver_path = "C:\Development\chromedriver.exe"
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
# chrome_options = Options()
# chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# chrome_options.add_argument(f'user-agent={user_agent}')
# chrome_options.add_experimental_option("detach", True)
# chrome_service = Service(chrome_driver_path)
# browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
# browser.get("https://www.linkedin.com/jobs/search/?currentJobId=3677059699&f_AL=true&f_WT=2&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")
# time.sleep(2)
# sign_in=browser.find_element(By.XPATH,'/html/body/div[3]/a[1]')
# time.sleep(2)
# sign_in_url = sign_in.get_attribute('href')
# browser.get(sign_in_url)
# username = browser.find_element(By.NAME,'session_key')
# time.sleep(2)

# username.send_keys("ijenrandy2@gmail.com")
# password = browser.find_element(By.NAME,'session_password')
# time.sleep(2)

# password.send_keys("linkedinWhizx1?")

# sign_in_button = browser.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
# time.sleep(2)
# sign_in_button.click()

# jobs = browser.find_elements(By.TAG_NAME,'a')
# for job in jobs:
#     job_link = job.get_attribute('href')
#     print(job_link)

    # if job_link is not None:
    #     browser.get(job_link)
    #     


# /html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button


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
EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
FILE_PATH = os.environ['FILE_PATH']

chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(fr'--user-data-dir={FILE_PATH}')
#---------------------------------------------------------------------
#added this argument to retrive chrome data *which my linked credentials already login, to skip CAPTCHA
# chrome_options.add_argument(fr'--profile-directory=Profile 10')
#---------------------------------------------------------------------
chrome_options.add_argument("--start-maximized")
chrome_service = Service(executable_path="C:\Development\chromedriver.exe")
driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3677059699&distance=25&f_AL=true&f_WT=2&geoId=102257491&keywords=python%20developer")

jobs = driver.find_elements(By.CSS_SELECTOR,'div.job-card-container')
jobs_links = []
for job in jobs:
    job_link = job.find_element(By.TAG_NAME,'a')
    jobs_links.append(job_link.get_attribute('href'))

for job_link in jobs_links:

    if job_link is not None:
        driver.get(str(job_link))
        next_button = driver.find_element(By.CSS_SELECTOR,'button.artdeco-button--primary')
        next_button.click()
        next_button = driver.find_element(By.CSS_SELECTOR,'button.artdeco-button--primary')
        next_button.click()
        next_button = driver.find_element(By.CSS_SELECTOR,'button.artdeco-button--primary')
        next_button.click()
        next_button = driver.find_element(By.CSS_SELECTOR,'button.artdeco-button--primary')
        next_button.click()
        next_button = driver.find_element(By.CSS_SELECTOR,'button.artdeco-button--primary')
        next_button.click()

        # years_of_experience = driver.find_element(By.CSS_SELECTOR,'input.artdeco-text-input--input')
        # years_of_experience.send_keys('5')

        # # next_button.click()

        # try:
        #     showmore_link = WebDriverWait(driver,10.0).until(EC.element_to_be_clickable((By.NAME,'urn:li:fsd_formElement:urn:li:jobs_applyformcommon_easyApplyFormElement:(3660211470,92690155,multipleChoice)')))
        #     showmore_link.click()

        # except ElementClickInterceptedException:
        #     print("Trying to click on the button again")
        #     driver.execute_script("arguments[0].click()", showmore_link)

        # review_button = driver.find_element(By.CSS_SELECTOR,'button.artdeco-button--primary')
        # review_button.click()
        # review_button.click()

        time.sleep(3)
    else:
       pass    

