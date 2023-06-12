import requests
from datetime import datetime,timedelta
from notification_manager import NotificationManager
from flight_data import FlightData
import os
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.FLIGHT_SEARCH_ENDPOINT="https://api.tequila.kiwi.com"
        self.FLIGHT_SEARCH_API_KEY = os.environ.get("FLIGHT_SEARCH_API_KEY")

    def get_city_iata_code(self,sheet_data):
    
        for data in sheet_data:
            if data["city"] in data:

                flight_search_headers = {
                    "apikey":self.FLIGHT_SEARCH_API_KEY,
                    "Content-Type": "application/json",
                }
                flight_search_params = {
                    "term":data["city"],
                    "loacation_types":"city"
                }

                response=requests.get(f"{self.FLIGHT_SEARCH_ENDPOINT}/locations/query",params=flight_search_params,headers=flight_search_headers)
                data["iataCode"]=response.json()["locations"][0]["code"]

    def get_city_flight_price(self,sheet_data):
        today = datetime.now()
        tomorrow = today + timedelta(days=1)
        six_months_time = today + timedelta(days=180)
        return_time_from = today + timedelta(days=7)
        return_time_to = today + timedelta(days=28)
        for data in sheet_data:
            flight_search_headers = {
                        "apikey":self.FLIGHT_SEARCH_API_KEY,
                        "Content-Type": "application/json",
                    }
            flight_search_params = {
                        "fly_from":"LON",
                        "fly_to":data["iataCode"],
                        "date_from":tomorrow.strftime("%d/%m/%Y"),
                        "date_to":six_months_time.strftime("%d/%m/%Y"),
                        "return_from":return_time_from.strftime("%d/%m/%Y"),
                        "return_to":return_time_to.strftime("%d/%m/%Y"),
                        "curr":"GBP"
                    }
            response = requests.get(f"{self.FLIGHT_SEARCH_ENDPOINT}/v2/search",params=flight_search_params,headers=flight_search_headers)
            flight_data =response.json()["data"][0]
            flight_price = response.json()["data"][0]["price"]
            if data["lowestPrice"] > flight_price:
                flightdata = FlightData(
                    price=flight_price,
                    origin_city=flight_data["cityFrom"],
                    origin_airport=flight_data["flyFrom"],
                    destination_city=flight_data["cityTo"],
                    destination_airport=flight_data["cityFrom"],
                    out_date=flight_data["route"][0]["local_departure"].split("T")[0],
                    return_date=flight_data["route"][1]["local_departure"].split("T")[0]

                )
                notify = NotificationManager()
                notify.send_price_alert_sms(flightdata)
            else:
                return False
    
