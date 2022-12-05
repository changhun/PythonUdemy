"""
import TOKEN
from bs4 import BeautifulSoup
import requests


#URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"
URL = "https://www.billboard.com/charts/hot-100/"
date = input("Which date you want to go back? (Type yyyy-mm-dd): ")
URL = URL + date + "/"

response = requests.get(URL)
content = response.text
soup = BeautifulSoup(content, "html.parser")
#title_tags = soup.find_all(name="h3", class_="c-title")
title_tags = soup.select("li h3")

titles = [tag.getText() for tag in title_tags[0:100]]
i = 0
for title in titles:
    print(i, title.strip())
    i += 1


print(TOKEN.CLIENT_ID)
"""
import TOKEN
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=TOKEN.CLIENT_ID,
        client_secret=TOKEN.CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)