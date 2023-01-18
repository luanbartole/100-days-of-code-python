import requests, time
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Web Request and Crawler
response = ""
while response == "":
    try:
        response = requests.get(url=URL)
        break
    except requests.exceptions.ConnectionError:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(10)
        print("Was a nice sleep, now let me continue...")
        continue

movies_web_page = response.text
soup = BeautifulSoup(movies_web_page, "html.parser")
movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies.reverse()

# Creating and writing in the file.
with open("best_movies", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
