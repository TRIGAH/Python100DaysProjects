import requests
from bs4 import BeautifulSoup
import pandas as pd
baseurl = "https://www.klarna.com//"

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}
s=requests.Session()
#Getting all Links on the website
urls_list = []
sub_urls_list=[]
sub_sub_urls_list=[]
products_urls_list=[]
def scrape_categories():
    site = "https://www.klarna.com/us/deals/"
    r = s.get(site,headers=headers)
    #converting the text
    soup = BeautifulSoup(r.text,'html.parser')
    for i in soup.find_all('a',class_="sc-gsnTZi gEbeYu sc-hAZoDl eayMnK sc-TRNrF hfrFoC menu-item"):
        href = i.attrs['href']
        if  href.startswith('/'):
            site = 'https://www.klarna.com' + href
            if site not in urls_list:
                urls_list.append(site)
scrape_categories() 
print(len(urls_list))

def scrape_sub_categories():
    for sub_url in urls_list:
        r = s.get(sub_url,headers=headers)
        soup = BeautifulSoup(r.text,'html.parser')  
        for i in soup.find_all('a', class_="css-19g0jcr"):
            href = i.attrs['href']
            if href.startswith('/'):
                site = 'https://www.klarna.com' + href
            if site not in sub_urls_list:
                sub_urls_list.append(site)
scrape_sub_categories()
print(len(sub_urls_list))

def scrape_sub_sub_categories():
    for sub_sub_url in sub_urls_list:
        r = s.get(sub_sub_url,headers=headers)
        soup = BeautifulSoup(r.text,'html.parser')
        for i in soup.find_all('a', class_="css-1p6tzrb"):
            href = i.attrs['href']
            if href.startswith('/'):
                site = 'https://www.klarna.com' + href
            if site not in sub_sub_urls_list:
                sub_sub_urls_list.append(site)    
scrape_sub_sub_categories()   
print(len(sub_sub_urls_list))

def scrape_products_urls():  
    for url in sub_sub_urls_list:
        r = s.get(url,headers=headers)
        soup = BeautifulSoup(r.text,'html.parser')
        for i in soup.find_all('div', class_="k6oEmfY83J css-6r3upd"):
            for link in i.find_all('a', href=True):
               href = link.attrs['href']
            if href.startswith('/'):
                site = 'https://www.klarna.com' + href
            if site not in products_urls_list:
                products_urls_list.append(site)  
scrape_products_urls()
print(len(products_urls_list))



# r = requests.get('https://www.klarna.com/us/shopping/cl/cl67/Shavers-Trimmers/?cat=58129112-60542253')

# soup = BeautifulSoup(r.content, 'lxml')

# productlist = soup.find_all('div', class_='k6oEmfY83J css-6r3upd')

# #  
# productlinks = []
# klarnalist = []
# for item in productlist:
#     for link in item.find_all('a', href=True):
#         productlinks.append(baseurl + link['href'])
# print(len(productlinks))

# # testlink = 'https://www.klarna.com/us/shopping/pl/cl67/4457312/Shavers-Trimmers/Philips-OneBlade-QP2520/'
# for link in productlinks:
#     r = requests.get(link,headers=headers) 
#     soup = BeautifulSoup(r.content, 'lxml')

#     store_name = soup.find('div',class_='css-1u8qly9')
#     store_url = soup.find('a', class_='XzwMZLLeA1', href=True)
#     try:
#        store_price = soup.find('div', class_='lXMIuQuWeR').text
#     except:
#         store_price='No Price'   
#     print(store_name['aria-label'],baseurl+store_url['href'],store_price)

#     product = {
#         'store_name':store_name['aria-label'],
#         'store_url':baseurl+store_url['href'],
#         'store_price':store_price
#     }
#     klarnalist.append(product)
#     print('Saving',product['store_name'])

# df = pd.DataFrame(klarnalist)    
# print(df.head(20))
