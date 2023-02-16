from itertools import product
import json
from zoneinfo import available_timezones

with open("async-webscraping-reviews.json") as amazon_reviews:
    data = json.load(amazon_reviews)
    amazon_product_list=[]
    for x in range(0,83):
        title=data["title"][str(x)]
        price=data["price"][str(x)]
        availability=data["avail"][str(x)]

        amazon_products={
            "title":title,
            "price":price,
            "availability":availability,
        }  
        amazon_product_list.append(amazon_products)  

print(amazon_product_list)