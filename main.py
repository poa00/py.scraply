import requests
from bs4 import BeautifulSoup as bs


URL = "https://www.olx.pl/oferty/q-reima-kombinezon-92/?search%5Border%5D=created_at%3Adesc"

page = requests.get(URL)
soup = bs(page.content, "html.parser")
offers = soup.find_all("table", class_="fixed")

for every in offers:
    name = every.find("a", class_="marginright5").find("strong").get_text()
    price = every.find("p", class_="price").find("strong").get_text()
    
    print("\nName: " + name)
    print("Price: " + price)


