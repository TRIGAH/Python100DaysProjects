import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
MY_EMAIL = "ijenrandy2@gmail.com"
MY_PASSWORD = "conjgpvrczhkxlqo"
product_url = "https://www.amazon.com/dp/B099K1QJ2Q/ref=syn_sd_onsite_desktop_0?ie=UTF8&psc=1&pf_rd_p=0c4daa46-238c-491d-9522-631142ac3b5a&pf_rd_r=9NR6XJPNP7CD9KS54A2D&pd_rd_wg=ntCYX&pd_rd_w=fNvc9&pd_rd_r=25c9d67a-1e35-405d-886d-98212dea3081"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"

}

response = requests.get(product_url,headers=headers)
soup=BeautifulSoup(response.text,"lxml")

product_title = soup.select_one("#productTitle").getText()
product_price=soup.find("span","a-offscreen").getText().split("$")[1]
product_link = soup.select_one("#bylineInfo")['href']

if float(product_price) < 200:
    with SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Amazon Price Alert\n\n{product_title} now at {product_price}\n https://www.amazon.com{product_link}"
        )  
    print("Email Sent")        