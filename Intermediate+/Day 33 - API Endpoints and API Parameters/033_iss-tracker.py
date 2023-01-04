import requests
import smtplib
import time
from datetime import datetime

user_email = "email@gmail.com"
user_password = "password"
target_email = "email@gmail.com"

# Brazil general coordinates
MY_LAT = -14.235004
MY_LNG = -51.925282


def iss_is_overhead():
    """Checks if the ISS it's right above your coordinates."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # Gets the current position of the ISS
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_pos = (longitude, latitude)

    iss_pos = (MY_LNG, MY_LAT)

    # If the ISS Position matches my position within an 5 margin error.
    if MY_LNG - 5 <= iss_pos[0] <= MY_LNG + 5 and MY_LAT - 5 <= iss_pos[1] <= MY_LAT + 5:
        return True
    else:
        return False


def is_night():
    # Set the parameters for Sunrise-Sunset API
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    # Request the api for the data
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

    # Raise status if an error occur
    response.raise_for_status()

    # Turn the JSON requested data into variable
    data = response.json()

    # Tap into the sunrise and sunset values, get the hour and subtract 3 to get my timezone corrected time.
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 3
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 3
    time_now = datetime.now()

    # If it matches my position when it's dark outside.
    if sunset < time_now.hour < 24 or time_now.hour < sunrise:
        return True
    else:
        return False


while True:
    if iss_is_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user_email, user_password)
            connection.sendmail(
                from_addr=user_email,
                to_addrs=target_email,
                msg=f"Subject: ISS Right Above You! Go Look Outside! \n\nThe ISS is close to your location in this "
                    f"great night! \nTry to spot in the sky outside. "
            )
    time.sleep(60)
