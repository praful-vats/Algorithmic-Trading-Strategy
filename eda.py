import matplotlib.pyplot as plt

def plot_closing_prices(data, ticker):
    data['Close'].plot(figsize=(10, 6))
    plt.title(f'{ticker} Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.show()
