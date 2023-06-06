import requests
from datetime import datetime

APP_ID = "a398d9bf"
API_KEY = "e64d051a320d7748647f5d8c2fed10de"

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_POST_ENDPOINT = "https://api.sheety.co/06c48b7bb5e56383737b0d5c5942307b/mapsWorkouts/workouts"

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "Content-Type": "application/json",
}

exercise_params = {
    "query": input("Tell me which exercises you did: ")
}

exercise_response = requests.post(EXERCISE_ENDPOINT,json=exercise_params,headers=headers)
# print(exercise_response.json()["exercises"][0])

today = datetime.now()
sheety_headers = {
    "Authorization": "Bearer MapsuireierWWnhhknblknkldfnmBaka"
}
sheety_data = {
    "workout":{
        "date":today.strftime("%d/%m/%Y"),
        "time":today.strftime("%X"),
        "exercise":str(exercise_response.json()["exercises"][0]["user_input"]).title(),
        "duration":exercise_response.json()["exercises"][0]["duration_min"],
        "calories":exercise_response.json()["exercises"][0]["nf_calories"]
    },
}

sheety_response = requests.post(SHEETY_POST_ENDPOINT,json=sheety_data,headers=sheety_headers)
print(sheety_response.text)