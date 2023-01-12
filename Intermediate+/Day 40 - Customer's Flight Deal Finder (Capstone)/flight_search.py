import requests
from datetime import datetime, timedelta
from flight_data import FlightData

FLIGHT_LOCATION_API_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
FLIGHT_SEARCH_API_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
today = datetime.now()
six_months_from_now = today + timedelta(180)


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self, key):
        self.apiKey = key
        self.headers = {"apikey": self.apiKey}

    def get_iata_code(self, city: str):
        response = requests.get(url=FLIGHT_LOCATION_API_ENDPOINT, headers=self.headers, params={"term": city})
        response.raise_for_status()
        flight_data = response.json()
        iata_code = flight_data["locations"][0]["code"]
        return iata_code

    def get_cheap_flight(self, destination_city: str):
        query = {
            "fly_from": "LON",
            "fly_to": destination_city,
            "date_from": str(today.strftime("%d/%m/%Y")),
            "date_to": str(six_months_from_now.strftime("%d/%m/%Y")),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"

        }
        response = requests.get(url=FLIGHT_SEARCH_API_ENDPOINT, headers=self.headers, params=query)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
        except IndexError:
            # print(f"No flights found for {destination_city}.")
            query["max_stopovers"] = 1
            response = requests.get(url=FLIGHT_SEARCH_API_ENDPOINT, headers=self.headers, params=query)
            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {destination_city}.")
                return None
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

        return flight_data
