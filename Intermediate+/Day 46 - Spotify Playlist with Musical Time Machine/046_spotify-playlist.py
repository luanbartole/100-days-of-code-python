import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

spotify_client_id = os.environ["SPOTIFY_BILLBOARD_CLIENT_ID"]
spotify_secret = os.environ["SPOTIFY_BILLBOARD_CLIENT_SECRET"]
spotify_redirect_url = "https://www.google.com/"
URL = "https://www.billboard.com/charts/hot-100/"
songs = []
songs_uris = []

print("=" * 45)
print(" " * 12 + "Musical Time Machine")
print("=" * 45)
print("\nWhich year do you want to travel to?")
date = input("[Type the date in the format YYYY-MM-DD]: ")
year = date.split("-")[0]

# ============================================Web Scraping============================================

# Web Scraping - 100 Best songs of year input.
response = requests.get(url=f"{URL}{date}/")
hot_billboard_site = response.text
soup = BeautifulSoup(hot_billboard_site, "html.parser")

# Generate the list of songs
for song in soup.find_all(name="h3", class_="a-no-trucate"):
    songs.append(song.getText().strip())
print("\n"+"=" * 45)
print(" "*10+f"100 Best songs of {year}:")
print("=" * 45)
print(f"{songs}")

# ============================================Spotify============================================

# Create spotify object and authentication
spot = spotipy.Spotify(
    auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                              redirect_uri=spotify_redirect_url,
                              client_id=spotify_client_id,
                              client_secret=spotify_secret,
                              show_dialog=True,
                              cache_path="token.txt")
)
user = spot.current_user()["id"]

# Search the songs in spotify to get the Tracks URI.
print("\n"+"=" * 45)
print(" "*10+"Finding the songs in Spotify:")
print("=" * 45)
for song in songs:
    track = spot.search(q=f"track: {song} year: {year}", limit=1, type="track", offset=0)
    try:
        track_uri = track["tracks"]["items"][0]["uri"]
        songs_uris.append(track_uri)
        print(f"{song}: {track_uri}")
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creates a playlist and add the tracks.
playlist = spot.user_playlist_create(user=user, name=f"100 Best Songs of {year}", public=False, collaborative=False, description="Playlist auto-generated using python.")
spot.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)

print("\n"+"=" * 45)
print(" "*10+f"100 Best Songs of {year}")
print(" "*10+"was created successfully")
print("=" * 45)
