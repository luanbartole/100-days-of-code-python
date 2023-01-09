import requests
from datetime import datetime, timedelta

USERNAME = "your_username_here"
TOKEN = "your_token_here"
today = datetime.now()-timedelta(0)
today = today.strftime("%Y%m%d")
print(today)

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
READING_GRAPH_ENDPOINT = f"{GRAPH_ENDPOINT}/graph1"
PIXEL_ENDPOINT = f"{READING_GRAPH_ENDPOINT}/{today}"

# Used to create user.
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notminor": "yes"
}

# Used to create graph.
graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai"
}

# Used to create pixel.
create_pixel = {
    "date": today,
    "quantity": input("How many pages did you read today?")
}

# Used to update pixel.
update_pixel = {
    "quantity": "60"
}

# Used to secure your API Key
headers = {
    "X-USER-TOKEN":  TOKEN
}

# Creates the Pixela User.
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)


# Creates the Graph.
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# Creates a Pixel.
response = requests.post(url=READING_GRAPH_ENDPOINT, json=create_pixel, headers=headers)
print(response.text)

# Updates a Pixel.
# response = requests.put(url=PIXEL_ENDPOINT, json=update_pixel, headers=headers)
# print(response.text)

# Deletes the Graph.
# response = requests.delete(url=READING_GRAPH_ENDPOINT, headers=headers)
# print(response.text)