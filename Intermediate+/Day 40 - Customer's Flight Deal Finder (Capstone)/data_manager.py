import requests

SHEETY_ENDPOINT = "https://api.sheety.co/b573244ba0df7b737d4e04bec7a441a6/flightDeals/prices"
USERS_SHEETY_ENDPOINT = "https://api.sheety.co/b573244ba0df7b737d4e04bec7a441a6/flightDeals/users"
class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self, token: str):
        self.sheety_token = {
            "Authorization": f"Bearer {token}"
        }
        self.customer_data = {}

    def get_sheet(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=self.sheety_token)
        response.raise_for_status()
        sheet_data = response.json()
        return sheet_data["prices"]

    def update_sheet(self, row: dict, row_id: int):
        updated_row = {
            "price": {
                "iataCode": row["iataCode"]
            }
        }
        response = requests.put(url=SHEETY_ENDPOINT+f"/{row_id}", headers=self.sheety_token, json=updated_row)
        response.raise_for_status()

    def add_new_user(self, new_row: dict):
        response = requests.post(url=USERS_SHEETY_ENDPOINT, headers=self.sheety_token, json=new_row)
        response.raise_for_status()
        print(response.status_code)
        print(response.text)
        return response.status_code

    def get_customer_emails(self):
        customers_endpoint = USERS_SHEETY_ENDPOINT
        response = requests.get(customers_endpoint, headers=self.sheety_token)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data



