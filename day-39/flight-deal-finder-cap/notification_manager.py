import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.proxy_client = TwilioHttpClient()
        # self.proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        self.client = Client(account_sid, auth_token, http_client=self.proxy_client)
    
    def send_price_alert_sms(self,flightdata):
            message = self.client.messages \
                .create(
                body=
                f"""
                Low price alert!
                Only £{flightdata.price} to fly From
                {flightdata.origin_city}-{flightdata.origin_airport} to
                {flightdata.destination_city}-{flightdata.destination_airport},
                {flightdata.out_date} to {flightdata.return_date}.
                """,
                from_="+13613091765",
                to="+2348172829491"
            )
            print(message.status)
