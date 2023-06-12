#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData

SHEETY_POST_ENDPOINT = "https://api.sheety.co/06c48b7bb5e56383737b0d5c5942307b/mapsWorkouts/workouts"

sheet_response = requests.get("https://api.sheety.co/06c48b7bb5e56383737b0d5c5942307b/myFlightDeals/prices")
sheet_data=sheet_response.json()["prices"]
# x=10
# lowest_prices = [price["lowestPrice"] for price in sheet_data ]

# def is_lower_price(lowest_prices):
#     if(min(lowest_prices)>x):
#         return True
#     else:
#         return False
    
# if is_lower_price(lowest_prices):
#     print("Sending.....SMS")

flight = FlightSearch()
# flight.get_city_iata_code(sheet_data)

# data = DataManager()
# data.add_codes_to_sheet(sheet_data)


flight.get_city_flight_price(sheet_data)




# flightdata = FlightData()

