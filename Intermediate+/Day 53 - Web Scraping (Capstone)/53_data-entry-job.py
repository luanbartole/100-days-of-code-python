import requests, time, json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


ZILLOW_URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.83501662207031%2C%22east%22%3A-122.03164137792969%2C%22south%22%3A37.55733345439207%2C%22north%22%3A37.99260877508999%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
FORM_URL = "https://forms.gle/LkRBYLCVBUCXsvad7"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
}

# ------------------------------Beautiful Soup------------------------------
# Scrape Price, Link and Addresses of Zillow.
response = requests.get(url=ZILLOW_URL, headers=headers)
response.raise_for_status()
data = response.text
soup = BeautifulSoup(data, "html.parser")

test = soup.findAll("script", attrs={"type": "application/json"})
rent_data = test[1].text
rent_data = rent_data.replace("<!--", "")
rent_data = rent_data.replace("-->", "")
rent_data = json.loads(rent_data)

rent_prices = []
rent_urls = []
rent_address = []

for x in rent_data["cat1"]["searchResults"]["listResults"]:
    # Extract prices
    try:
        rent_prices.append(x["price"].strip("+/mo"))
    except KeyError:
        rent_prices.append(x["units"][0]["price"].strip("+/mo"))

    # Extract urls
    if "https" in x["detailUrl"]:
        rent_urls.append(x["detailUrl"])
    else:
        rent_urls.append("https://www.zillow.com"+x["detailUrl"])

    # Extract addresses
    rent_address.append(x["address"])

# ------------------------------Selenium------------------------------
service = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

for _ in range(len(rent_prices)):
    driver.get(FORM_URL)
    questions = driver.find_elements(By.CSS_SELECTOR, "div.Xb9hP input")
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    questions[0].send_keys(rent_address[_])
    questions[1].send_keys(rent_prices[_])
    questions[2].send_keys(rent_urls[_])
    submit_button.click()






