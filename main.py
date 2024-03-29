import requests
from bs4 import BeautifulSoup as bs


URL = "https://www.olx.pl/oferty/q-reima-kombinezon-92/?search%5Border%5D=created_at%3Adesc"

page = requests.get(URL)
soup = bs(page.content, "html.parser")
offers = soup.find_all("div", class_="offer-wrapper")

print("{} offers found".format(len(offers)))

for offer in offers:
    offer_table = offer.find("table", class_="fixed")
    id = offer_table.get("data-id")
    name = offer_table.find("a", class_="marginright5").find("strong").get_text()
    price = offer_table.find("p", class_="price").find("strong").get_text()
    delivery = False
    if offer_table.find("div", class_='olx-delivery-icon'):
        delivery = True
    link = offer_table.find("a", class_="thumb").get("href")
    img = offer_table.find("img", class_="fleft").get("src")

    breadcrumb = offer_table.find("td",class_="bottom-cell").find_all("small",class_="breadcrumb")
    loc = breadcrumb[0].get_text().strip()
    date = breadcrumb[1].get_text().strip()
    
    print("{} | {}  |  {}  |  {}".format(id, price, delivery, name))
