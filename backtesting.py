import matplotlib.pyplot as plt

def backtest_strategy(data):
    data['Market Return'] = data['Close'].pct_change()
    data['Strategy Return'] = data['Market Return'] * data['Position'].shift(1)
    data['Cumulative Market Return'] = (1 + data['Market Return']).cumprod()
    data['Cumulative Strategy Return'] = (1 + data['Strategy Return']).cumprod()
    return data

def plot_returns(data):
    data[['Cumulative Market Return', 'Cumulative Strategy Return']].plot(figsize=(10, 6))
    plt.title('Market vs Strategy Returns')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.show()
