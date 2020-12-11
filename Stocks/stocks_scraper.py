# File to scarpe stocks
from bs4 import BeautifulSoup
import requests
import random
# Need to change this when I make a package
from stocks import Stocks

stocks_array = [ "ORCL", "FB", "MSFT", "AMZN", "GOOGL", "AAPL"]
stock = Stocks()

for stock_name in stocks_array :
    url = "https://finance.yahoo.com/quote/{}/".format(stock_name)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    quantity = random.randint(1,10)
    stock.add_new_stock(stock_name, price.replace(",", ""), quantity)

print("######", stock)

