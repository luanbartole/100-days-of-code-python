import os
import requests
import datetime as dt
from twilio.rest import Client

# API Keys and Endpoints
# 1 - Market Stack = Stocks Closing Prices
# 2 - News API = News about Stocks
# 3 - TWILIO = Send SMS if stock change above threshold
MARKETSTACK_API_ENDPOINT = "http://api.marketstack.com/v1/eod"
MARKETSTACK_API_KEY = os.environ.get("MARKETSTACK_API_KEY")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
PHONE_A = os.environ.get("PHONE_A")
PHONE_B = os.environ.get("PHONE_B")

# Threshold percentage, stock and company name.
THRESHOLD = 5
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def stock_price_diff():
    """Returns the percentage difference of yesterday and two days ago stock closing prices"""

    # Gets the date of yesterday and two days ago.
    yesterday = str(dt.datetime.now() - dt.timedelta(4))[:-2]
    yesterday = yesterday[:10]
    two_days_ago = str(dt.datetime.now() - dt.timedelta(5))[:-2]
    two_days_ago = two_days_ago[:10]

    # Parameters for the API request.
    stock_api_params = {
        "access_key": MARKETSTACK_API_KEY,
        "symbols": STOCK,
        "date_from": two_days_ago,
        "date_to": yesterday
    }

    # API request.
    response = requests.get(MARKETSTACK_API_ENDPOINT, stock_api_params)
    response.raise_for_status()
    stock_data = response.json()

    # Closing Prices
    yesterday_close = stock_data["data"][0]["close"]
    two_days_ago_close = stock_data["data"][1]["close"]

    # Calculates the percentage difference between the two and returns it.
    percent_diff = round(((yesterday_close - two_days_ago_close) / two_days_ago_close) * 100)
    return percent_diff


def stock_news():
    """Returns the articles to help identify why was the threshold price change broken"""
    news_api_params = {
        "q": COMPANY_NAME,
        "language": "en",
        "from": "2023-01-09",
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
        "pageSize": 3
    }

    response = requests.get(NEWS_API_ENDPOINT, news_api_params)
    response.raise_for_status()
    news_data = response.json()
    return news_data["articles"]


def send_sms(text: str):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=text,
        from_=PHONE_A,
        to=PHONE_B
    )
    print(message.status)


# Pulls the percentage difference of the stock and the articles about the company.
stock_diff = stock_price_diff()
if abs(stock_diff > THRESHOLD):
    articles = stock_news()
    stock_string = ""
    stock_sms = ""

    # Create the stock string based on the price percentage difference.
    if stock_diff > 0:
        stock_string = f"🔺{abs(stock_price_diff())}%"
    else:
        stock_string = f"🔻{abs(stock_price_diff())}%"

    # Writes the SMS with the stock difference and articles about it.
    for article in articles:
        stock_sms += f"{STOCK}: {stock_string} \nHeadline: {article['title']} \nBrief: {article['description']}\n\n"

    send_sms(stock_sms)
