import requests
import os
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_token =os.environ.get("SHEETY_TOKEN")

    def add_codes_to_sheet(self,sheet_data):
        for data in sheet_data:
            sheet_put_endpoint =f"https://api.sheety.co/06c48b7bb5e56383737b0d5c5942307b/myFlightDeals/prices/{data['id']}"
            sheety_headers = {
               "Authorization": self.sheety_token
            }
            sheet_query = {
               "price":{
                  "iataCode":data["iataCode"]
               }
            }
            sheet_update_response=requests.put(sheet_put_endpoint,json=sheet_query,headers=sheety_headers)
            print(sheet_update_response.text)
