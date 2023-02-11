from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# =========================================Start Website and Language=========================================
# Set service and driver
service = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the game and wait 5 seconds for load screen.
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)

# Select the language and wait 5 seconds for load screen.
language = driver.find_element(By.ID, "langSelect-PT-BR")
language.click()
time.sleep(2)


# =========================================Cookie Stats=========================================
# Global Stats
cookie_stats = []
cookies_per_second = 0
cookie_money = 0
cost = 0
cookie = driver.find_element(By.ID, "bigCookie")


def update_stats():
    global cookie_stats
    global cookie_money
    global cookies_per_second

    cookie_stats = driver.find_element(By.ID, "cookies").text.split("\n")
    cookies_per_second = float(cookie_stats[1].split(" ")[-1])
    try:
        cookie_money = int(cookie_stats[0].split(" ")[0])
    except ValueError:
        cookie_money = int(cookie_stats[0].split(" ")[0].strip(","))


def update_cost():
    global cost
    try:
        cost = int(upgrade.find_element(By.CLASS_NAME, "price").text)
    except ValueError:
        cost = int(upgrade.find_element(By.CLASS_NAME, "price").text.strip(","))


# =========================================Cookie Clicker Automated Game=========================================

# Start and end of the game (to ensure 5 min gameplay only instead of running until infinity).
game_time = time.time()
end_time = time.time() + 60 * 20

# Runs the program for 5 minutes.
while game_time < end_time:
    current_time = time.time()
    time_until_upgrade = time.time() + 5

    # Clicks the cookie for 5 seconds.
    while current_time < time_until_upgrade:
        cookie.click()
        current_time = time.time()

    update_stats()
    upgrades_available = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")

    # Check if there is any upgrades available and buy them (most expensive -> least expensive).
    if len(upgrades_available) != 0:
        # Buy order: last upgrade (usually more expensive) < first upgrade (usually less expensive)
        for upgrade in reversed(upgrades_available):
            update_cost()
            # Buy the upgrade while it can afford it.
            while cookie_money > cost:
                upgrade.click()
                update_stats()
                update_cost()

    # Updates the game current time and print time left to end of game.
    game_time = time.time()
    print(f"Minutes left: {(end_time - game_time)/60: .1f}")
# End of the Game
print(f"Congrats! Your total Cookies per Second was {cookies_per_second}")
