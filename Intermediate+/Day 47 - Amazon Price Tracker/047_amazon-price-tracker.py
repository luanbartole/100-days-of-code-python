import encodings
import os
import requests
from bs4 import BeautifulSoup
import smtplib
import html

sender_email = os.environ.get("PYTHON_EMAIL")
sender_password = os.environ.get("PYTHON_EMAIL_PASSWORD")
user_email = os.environ.get("USER_EMAIL")


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
}
# ====================================User Input and Website====================================
print("=" * 45)
print(" " * 12 + "Amazon Price Tracker")
print("=" * 45)
url = input("Product URL: ")
desired_price = float(input("Desired Price (No decimals): R$ "))

# Requests and soup class
response = requests.get(url=url, headers=headers)
amazon_product = response.content
soup = BeautifulSoup(amazon_product, "html.parser")
product_name = soup.find(name="span", id="productTitle").get_text().strip()


# ====================================Scrape the Product Price(s)====================================
def price_into_float(price_string):
    price_without_currency = price_string.split("R$ ")[1]
    price_float = float(price_without_currency.replace(",", "."))
    return price_float


# Main Price and Alternative Price (New/Used by other sellers on amazon)
price = soup.find(name="span", id="price").getText().replace(u'\xa0', ' ')
alternative_prices = soup.find_all(name="a", class_="a-size-mini a-link-normal")

# Product Prices = [0] Main Price / # [1] Alternative Used Lowest Price / [2] Alternative New Lowest Price
product_prices = [price_into_float(price)]
prices_label = ["Main", "Used", "New"]

for price_index in range(len(alternative_prices)):
    alternative_prices[price_index] = alternative_prices[price_index].getText().replace(u'\xa0', ' ').strip(" ")
    alternative_prices[price_index] = alternative_prices[price_index].split(" ")
    alternative_prices[price_index] = "".join(alternative_prices[price_index][-2]) + " " \
                                      + "".join(alternative_prices[price_index][-1])
    product_prices.append(price_into_float(alternative_prices[price_index]))
    # print(f"a{price: .2f}a")

product_prices_with_currency = [price, alternative_prices[0], alternative_prices[1]]


# ====================================Email alert when price below preset value====================================
def lowest_price_offer(prices, maximum_price, condition="any"):
    low_offers = []
    no_used_product = False

    # condition: any = used low offers applies / new = only main or new low offers applies.
    if condition == "new":
        no_used_product = True

    for _ in range(len(prices)):
        if no_used_product and _ == 1:
            continue
        else:
            if prices[_] < maximum_price:
                low_offers.append(prices[_])
    try:
        lowest_offer = prices.index(min(low_offers))
        return prices_label[lowest_offer]
    except:
        return None

    # print(f"{prices_label[_]}: Not low enough! ({prices[_]})")
    # print(f"{prices_label[_]}: Low price offer! ({prices[_]})")


lowest_price = lowest_price_offer(product_prices, desired_price)
if lowest_price is not None:
    if len(product_name) > 20:
        product_title = product_name[:20]
    else:
        product_title = html.unescape(product_name)
    message = f"Subject: Amazon Price Alert! Low Price on '{product_title}...' \n\nProduct: {product_name}" \
              f"\nDesired Minimum Price: R${desired_price: .0f},00" \
              f"\nCurrent Price: {product_prices_with_currency[prices_label.index(lowest_price)]}" \
              f"\nProduct Condition: {lowest_price}"
    print(message)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(sender_email, sender_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=user_email,
            msg=f"{message}".encode("utf-8")
        )

# Allow user to add and see multiple price trackers (For future if I'm bored)
# Make the program create a text in which it saves the products_tracker.
# Let the user choose if he wants to run the product_tracker of if he wants to add another product to it.

# products_tracker = {
#     product_name: {
#         "minimum_price": desired_price,
#         "current_prices": product_prices
#     }
# }
# print(products_tracker)
