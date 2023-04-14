# stockanalyzer
This is a Python code that defines a class called StockAnalyzer which can be used to analyze stock data for a given company.

The class has several methods that allow for data retrieval and plotting.

The __init__ method takes in a ticker parameter which represents the ticker symbol for the desired company.

The get_google_finance_data method retrieves the current stock price and change in price from Google Finance for the given ticker symbol.

The get_yahoo_finance_data method retrieves the historical stock data for the given ticker symbol from Yahoo Finance, starting from the provided start_date.

The get_major_shareholders method retrieves a list of major shareholders for the given company from CNN Money.

The get_board_of_directors method retrieves a list of members of the board of directors for the given company from CNN Money.

The plot_stock_price method uses the get_yahoo_finance_data method to retrieve historical stock data and plots the adjusted close price over time starting from the provided start_date.

Lastly, the code creates an instance of the StockAnalyzer class for the Apple company with ticker symbol "AAPL", retrieves and prints the current stock price and change, retrieves and prints the major shareholders and board of directors, and plots the historical stock price starting from January 1, 2020.
