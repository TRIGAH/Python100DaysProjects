from multiprocessing.connection import wait
from urllib import response
from bs4 import BeautifulSoup
import grequests
import requests
import pandas as pd
url="https://www.amazon.co.uk/product-reviews/B01B5UZ4TA/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=1"
amazon_reviews_list=[]

def get_soup(url):
    resp = requests.get("http://localhost:8050/render.html",{'url':url,'wait':2})
    soup = BeautifulSoup(resp.text,"html.parser")
    return soup

def get_reviews(soup):
    amazon_reviews = soup.find_all("div",{"data-hook":"review"})
    try:
        for item in amazon_reviews:
            review={
            "product":soup.title.text.replace("Amazon.co.uk:Customer reviews:","").strip(),
            "title":item.find("a",{"data-hook":"review-title"}).text.strip(),
            "rating":float(item.find("i",{"data-hook":"review-star-rating"}).text.replace("out of 5 stars","").strip()),
            "body":item.find("span",{"data-hook":"review-body"}).text.strip(),
            }
            amazon_reviews_list.append(review)
    except:
        pass        

for x in range(1,10):
    soup=get_soup(f"https://www.amazon.co.uk/product-reviews/B01B5UZ4TA/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}")
    get_reviews(soup)
    print(len(amazon_reviews_list))
    if not soup.find("li",{"class":"a-disabled a-last"}):
        pass
    else:
        break

df=pd.DataFrame(amazon_reviews_list)
df.to_csv("amzon-reviews.csv")    
print("Finish....")


      
