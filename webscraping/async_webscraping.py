from bs4 import BeautifulSoup
import grequests
import pandas as pd

def get_urls():
    urls = []
    for x in range(1,5):
        urls.append(f'https://www.canoeandkayakstore.co.uk/collections/boats-canoe-canoes?page={x}')
    return urls

def get_data(urls):
    reqs = [grequests.get(link) for link in urls]
    resp = grequests.map(reqs)
    return resp

def parse(resp):
    amazon_product_list=[]
    for r in resp:
        soup=BeautifulSoup(r.text,"lxml") 
        product = soup.find_all("div",{"class":"product-grid-item__info"})   
        for item in product:
            product={
            "title":item.find_all("a")[0].text.strip(),
            "price":item.find("span",{"class":"product-grid-item-price"}).find_all("span")[0].text.strip(),
            "avail":item.find("span",{"class":"product-grid-item__info__availability--value"}).text.strip(),
            }
            amazon_product_list.append(product)
            print("Added: ",product)     
    return amazon_product_list;             

url=get_urls() 
resp = get_data(url)
df=pd.DataFrame(parse(resp))   
df.to_json("async-webscraping-reviews.json")  
df.to_excel("pandas_to_db.xlsx")   
print("File Created")