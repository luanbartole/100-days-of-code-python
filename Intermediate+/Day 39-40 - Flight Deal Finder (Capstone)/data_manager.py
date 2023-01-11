import requests

SHEETY_ENDPOINT = "https://api.sheety.co/b573244ba0df7b737d4e04bec7a441a6/flightDeals/prices"
class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self, token: str):
        self.sheety_token = {
            "Authorization": f"Bearer {token}"
        }

    def get_sheet(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=self.sheety_token)
        response.raise_for_status()
        sheet_data = response.json()
        return sheet_data["prices"]

    def update_sheet(self, row: dict, row_id: int):
        new_row = {
            "price": {
                "iataCode": row["iataCode"]
            }
        }
        response = requests.put(url=SHEETY_ENDPOINT+f"/{row_id}", headers=self.sheety_token, json=new_row)
        response.raise_for_status()

