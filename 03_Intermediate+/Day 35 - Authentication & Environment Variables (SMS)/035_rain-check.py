import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "your_api_key"

account_sid = "your_account_sid"
auth_token = "your_token"
# How many hours forward do you want to predict - 1 (max: 48)
prediction_hours = 12

weather_params = {
    # Brazil
    "lat": -14.235004,
    "lon": -51.925282,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()["hourly"]


def is_gonna_rain():
    raining_soon = False
    weather_hourly = weather_data[:prediction_hours]
    for _ in range(len(weather_hourly)):
        hour_data = weather_hourly[_]["weather"][0]
        hour_code = hour_data["id"]
        main_description = f"{hour_data['main']}: {hour_data['description'].capitalize()}"
        print(_, hour_code, main_description)
        if hour_code < 600:
            raining_soon = True
        else:
            pass
    return raining_soon


def send_sms(text):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=text,
        from_="phone_number_a",
        to="phone_number_b"
    )
    print(message.status)


if is_gonna_rain():
    send_sms("Catch the Bus! It's gonna rain.")
else:
    send_sms("You are good to go! Biking time!")
