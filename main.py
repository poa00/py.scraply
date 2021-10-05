import requests
from bs4 import BeautifulSoup as bs


URL = "https://www.olx.pl/oferty/q-reima-kombinezon-92/?search%5Border%5D=created_at%3Adesc"

page = requests.get(URL)
soup = bs(page.content, "html.parser")
offers = soup.find_all("table", class_="fixed")

print("{} offers found".format(len(offers)))

for every in offers:
    id = every.get("data-id")
    name = every.find("a", class_="marginright5").find("strong").get_text()
    price = every.find("p", class_="price").find("strong").get_text()

    print("{} | {}  |  {}".format(id, price, name))
