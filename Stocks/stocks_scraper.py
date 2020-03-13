# File to scarpe stocks
from bs4 import BeautifulSoup
import requests
import random

stocks = [ "ORCL", "FB", "MSFT", "AMZN", "GOOGL", "AAPL"]

f = open("scraped.html", "w")
for stock_name in stocks:
    url = "https://finance.yahoo.com/quote/{}/".format(stock_name)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.select_one("[class*='smartphone_Mt'] span").text
    number_of_stocks = random.randint(1,10)

