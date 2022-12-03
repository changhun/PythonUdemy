from bs4 import BeautifulSoup
import requests


#URL = "https://www.billboard.com/charts/hot-100/"
URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

#date = input("Which date you want to go back? (Type yyyy-mm-dd): ")
#URL = URL + date + "/"
#print(URL)

response = requests.get(URL)
content = response.text
soup = BeautifulSoup(content, "html.parser")
#title_tags = soup.find_all(name="h3", class_="c-title")
title_tags = soup.select("li h3")
# for tag in title_tags:
#    print(tag)
titles = [tag.getText() for tag in title_tags]
for title in titles:
    print(title.strip())
#print(titles)

