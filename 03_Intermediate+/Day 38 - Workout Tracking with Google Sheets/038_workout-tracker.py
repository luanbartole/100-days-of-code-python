import requests
import os
from datetime import datetime

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/b573244ba0df7b737d4e04bec7a441a6/myWorkouts/workouts"
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")
APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
today = datetime.now()
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
params = {
    "query": input("Exercises done: "),
    "gender": "male",
    "weight_kg": 85,
    "height_cm": 175,
    "age": 19
}
sheety_token = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

def add_row(exercise: str):
    new_row = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["user_input"].capitalize(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=new_row, headers=sheety_token)
    print(response.status_code)

# Get data about the exercises and add then into the google sheet.
response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=headers, json=params)
exercise_data = response.json()
for exercise in exercise_data["exercises"]:
    add_row(exercise)
