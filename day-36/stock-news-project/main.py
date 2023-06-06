import requests
import os
from datetime import date,timedelta
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT ="https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

account_sid = "AC85e7b370a505c56541ddd89934c6056f"
auth_token = os.environ.get("AUTH_TOKEN")
print(auth_token)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_data = response.json()["Time Series (Daily)"]

stock_data_dates=[key for (key,value) in stock_data.items()]
yesterday_date = stock_data_dates[0]
day_before_yesterday_date = stock_data_dates[1]

yesterday_stock_close_price=stock_data[yesterday_date]["4. close"]
day_before_yesterday_stock_close_price=stock_data[day_before_yesterday_date]["4. close"]

print(yesterday_stock_close_price)
print(day_before_yesterday_stock_close_price)

def get_percentage_increase(num_a, num_b):
    return abs(((num_a - num_b) / num_b) * 100)

percent=get_percentage_increase(float(yesterday_stock_close_price), float(day_before_yesterday_stock_close_price))
print(get_percentage_increase(1568.3600,1643.0000))
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_parameters = {
    "q":"tesla",
    "from":stock_data_dates[1],
    "sortBy":"publishedAt",
    "apiKey":NEWS_API_KEY
}
response = requests.get(NEWS_ENDPOINT,params=news_parameters)
stock_news_data = response.json()["articles"][0]

title=stock_news_data["title"]
description=stock_news_data["description"]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}

# client = Client(account_sid, auth_token, http_client=proxy_client)
# message = client.messages \
#     .create(
#     body=
    
#     f"""
#     {STOCK}: 🔺{percent}%
#     Headline: Were Hedge Funds Right About Piling Into {COMPANY_NAME}. ({STOCK})?. 
#     Brief: {description}.
#     """,
#     from_="+13613091765",
#     to="+2348172829491"
# )
# print(message.status)
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

