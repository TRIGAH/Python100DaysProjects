import requests
import webhook
import json

headers = {
    "content-type":"application/json",
    "Authorization": 'Bearer sk_test_785696d694e604c7fbdc9a4048c7c1fc844bbf19',
}

#Checks if it is a valid account number
verify_details = {
    "account_number":"0138659227",
    "bank_code":"058",
}
verify_url="https://api.paystack.co/bank/resolve"
verify = requests.get(verify_url,headers=headers,params=verify_details)
if verify.status_code == 200:
    bank_details = verify.json()["data"]
    create_recepient_details = { 
        "type": "nuban",
        "name": bank_details["account_name"],
        "account_number": bank_details["account_number"],
        "bank_code": "058",
        "currency": "NGN",
    }

    # Create a recepeint for transfer
    create_url="https://api.paystack.co/transferrecipient"
    create = requests.post(create_url,headers=headers,data=json.dumps(create_recepient_details))
    recepient_details = create.json()["data"]
    transfer_details ={
        "source": "balance",
        "amount": "1500",
        "recipient": recepient_details["recipient_code"],
        "reason": "Holiday Flexing",
    }


    # Transfer money to recepient
    send_url ="https://api.paystack.co/transfer"
    send = requests.post(send_url,headers=headers,data=json.dumps(transfer_details),timeout=5)
    if send.status_code == 200:
        #Check if Transfer was successful
        confirm_url = "https://hooks.zapier.com/hooks/catch/12574428/bfrd9e5/"
        confirm = requests.get(confirm_url,timeout=5)
        print("Tranfer Successfull")


# r = requests.get("https://api.paystack.co/bank/")
# print(r.json()["data"])
# 0157631451

        # headers = {
        #         "content-type":"application/json",
        #         "Authorization": 'Bearer sk_test_785696d694e604c7fbdc9a4048c7c1fc844bbf19',
        # }

        # # Verification of Bank Details
        # verify_url="https://api.paystack.co/bank/resolve"
        # verify_bank_details = {
        #     "account_number":self.account.account_no,
        #     "bank_code":"058",
        # }
        # verify = requests.get(verify_url,headers=headers,params=verify_bank_details)
        # print(verify.json())
        # print("Account Number Exists")

        # # Create Recepient
        # create_recepient = { 
        #     "type": "nuban",
        #     "name": "Ijen Gandeoron Randy",
        #     "account_number": self.account.account_no,
        #     "bank_code": "058",
        #     "currency": "NGN",
        # }

        # create_recepient_url="https://api.paystack.co/transferrecipient"
        # response = requests.post(create_recepient_url,headers=headers,data=json.dumps(create_recepient))
        # print(response.json())

        # # Transfer Money to Recepient
        # transfer_details = {
        #         "source":self.source,
        #         "amount": self.amount+"00",
        #         "recipient":self.recipient,
        #         "reason": self.reason,
        # }

      

        # send_url ="https://api.paystack.co/transfer"

        # confirm_url = "https://hooks.zapier.com/hooks/catch/12574428/bfrd9e5/"
        # try:
        #     send = requests.post(send_url,headers=headers,data=json.dumps(transfer_details),timeout=10)
        #     print(send.json())
        #     confirm = requests.get(confirm_url,timeout=5)
        #     print(confirm.json())
        #     print("Tranfer Successfull")
        #     print(self.amount)
        # except Timeout:
        #     print('Timeout has been raised.')