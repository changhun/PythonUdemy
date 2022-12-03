from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# titleline = soup.select(".titleline")
# for tag in titleline:
#     #print(tag.getText())
#     print(tag.text)

#print(soup.select_one(".titleline").select_one('a'))
#print(soup.select_one(".titleline").a)

article_tag = soup.select_one(".titleline").a
article_text = soup.select_one(".titleline").a.text
article_link = soup.select_one(".titleline").a.get("href")
#print(article_link)
article_upvote = soup.select_one(".score").getText().split()[0]
print(article_upvote)






# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
# #print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag)
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(soup.find(name="h1", id="name").string)
# print(soup.find(name="h1", id="name").getText())
#
#
# print(soup.select_one("p a"))
# print(soup.select_one("#name"))
#
# print(soup.select(selector=".heading"))
# print(soup.select(".heading"))
