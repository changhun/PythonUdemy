from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2")
content = response.text
soup = BeautifulSoup(content, "html.parser")

h3tag_list = soup.find_all("h3", class_="jsx-4245974604")

movies = [h3tag.getText() for h3tag in h3tag_list]
movies.sort()
print(movies)