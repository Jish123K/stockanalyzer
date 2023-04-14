import requests

from bs4 import BeautifulSoup

import yfinance as yf

import matplotlib.pyplot as plt

class StockAnalyzer:

    

    def __init__(self, ticker):

        self.ticker = ticker

    

    def get_google_finance_data(self):

        url = f"https://www.google.com/finance/quote/{self.ticker}"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        price = soup.find_all("div", {"class": "YMlKec fxKbKc"})[0].find("span").text

        change = soup.find_all("div", {"class": "YMlKec fxKbKc"})[1].find("span").text

        return (price, change)

    

    def get_yahoo_finance_data(self, start_date):

        data = yf.download(self.ticker, start=start_date)

        return data

    

    def get_major_shareholders(self):

        url = f"https://money.cnn.com/quote/shareholders/shareholders.html?symb={self.ticker}"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        shareholders = []

        for row in soup.find_all("table", {"class": "wsod_dataTable wsod_dataTableBig"})[0].find_all("tr")[1:]:

            name = row.find_all("td")[0].text

            shares = row.find_all("td")[1].text

            shareholders.append((name, shares))

        return shareholders

    

    def get_board_of_directors(self):

        url = f"https://money.cnn.com/quote/profile/profile.html?symb={self.ticker}"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        directors = []

        for row in soup.find_all("table", {"class": "wsod_dataTable"})[0].find_all("tr")[1:]:

            name = row.find_all("td")[0].text

            title = row.find_all("td")[1].text

            age = row.find_all("td")[2].text

            pay = row.find_all("td")[3].text

            directors.append((name, title, age, pay))

        return directors

    

    def plot_stock_price(self, start_date):

        data = self.get_yahoo_finance_data(start_date)

        plt.plot(data["Adj Close"])

        plt.title(f"{self.ticker} Stock Price")

        plt.xlabel("Date")

        plt.ylabel("Price")

        plt.show()

stock = StockAnalyzer("AAPL") # Replace "AAPL" with the ticker symbol of your desired company

# Get the stock price and change from Google Finance

price, change = stock.get_google_finance_data()

print(f"Price: {price}")

print(f"Change: {change}")

# Get the major shareholders

shareholders = stock.get_major_shareholders()

for shareholder in shareholders:

    print(f"{shareholder[0]}: {shareholder[1]}")

# Get the board of directors

directors = stock.get_board_of_directors()

for director in directors:

    print(f"{director[0]} ({director[1]}) - Age: {director[2]}, Pay: {director[3]}")

# Plot the stock price from the input date using Yahoo Finance

start_date = "2020-01-01"

stock.plot_stock_price(start_date)

