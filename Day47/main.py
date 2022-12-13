import requests
from bs4 import BeautifulSoup
import lxml

#URL = 'https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463'
URL = 'https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904'

request_headers = {
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response = requests.get(URL, headers=request_headers)

html = response.text
#print(html)

soup = BeautifulSoup(html, "lxml")
#print(soup.prettify())

#price = soup.find(id="priceblock_ourprice").get_text()
#print(price)
#price = soup.select(".a-offscreen")
price_tag = soup.find(class_="a-price a-text-price a-size-medium apexPriceToPay").select_one("span")
price = price_tag.getText().split("$")[1]

print(price)