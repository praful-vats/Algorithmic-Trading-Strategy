import numpy as np

def calculate_metrics(data):
    total_return = data['Cumulative Strategy Return'][-1] - 1
    annualized_return = data['Strategy Return'].mean() * 252
    annualized_volatility = data['Strategy Return'].std() * np.sqrt(252)
    sharpe_ratio = annualized_return / annualized_volatility

    print(f'Total Return: {total_return * 100:.2f}%')
    print(f'Annualized Return: {annualized_return * 100:.2f}%')
    print(f'Annualized Volatility: {annualized_volatility * 100:.2f}%')
    print(f'Sharpe Ratio: {sharpe_ratio:.2f}')
