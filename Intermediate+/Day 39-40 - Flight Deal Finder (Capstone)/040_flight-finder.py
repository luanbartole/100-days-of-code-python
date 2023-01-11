import os
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch

# Get the Environment Variables = API keys, tokens and other sensible info.
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")
FLIGHT_API_KEY = os.environ.get("KIWI_TEQUILA_FLIGHT_API_KEY")
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
PHONE_A = os.environ.get("PHONE_A")
PHONE_B = os.environ.get("PHONE_B")

# Create the objects
notification_manager = NotificationManager(
    twilio_sid=ACCOUNT_SID,
    twilio_token=AUTH_TOKEN,
    twilio_phone_a=PHONE_A,
    twilio_phone_b=PHONE_B)
data_manager = DataManager(SHEETY_BEARER_TOKEN)
flight_search = FlightSearch(FLIGHT_API_KEY)


# Get the sheet
sheet_data = data_manager.get_sheet()

# Update the sheet with IATA Codes
for row_id in range(len(sheet_data)):

    # If there is any value for the iataCode key in the sheet_data:
    row = sheet_data[row_id]

    if row["iataCode"]:
        print("IATA Codes are already filled.")
    else:
        # Write the IATA Code value for the iataCode key in the current row.
        row["iataCode"] = flight_search.get_iata_code(row["city"])

        # Update the current row in the Google Sheets.
        data_manager.update_sheet(row, row_id+2)

        # Query the cheapest flight from London to the current row city.
        cheap_flight = flight_search.get_cheap_flight(row["iataCode"])

        # If the program found a cheap flight under the parameters given to.
        if cheap_flight:
            # If the flight is cheaper than the minimum price on Google Sheet, send a sms.
            if cheap_flight.price < row["lowestPrice"]:
                sms = f"Low price alert! Only £{cheap_flight.price} " \
                      f"to fly from {cheap_flight.origin_city}-{cheap_flight.origin_airport} " \
                      f"to {cheap_flight.destination_city}-{cheap_flight.destination_airport}, " \
                      f"from {cheap_flight.out_date} to {cheap_flight.return_date}."
                print(sms)
                notification_manager.send_sms(text=sms)
