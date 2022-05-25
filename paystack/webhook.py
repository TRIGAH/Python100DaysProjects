from urllib import response
import requests
import json

webhook_url="https://hooks.zapier.com/hooks/catch/12574428/bfrd9e5/"

data ={
    "name":"Maps",
    "talent":"Singing",
}
headers ={
    "Content-Type":"application/json"
}

r = requests.post(webhook_url,data=json.dumps(data),headers=headers)