from data_collection import get_data
from eda import plot_closing_prices
from feature_engineering import add_moving_averages
from strategy import generate_signals
from backtesting import backtest_strategy, plot_returns
from performance_metrics import calculate_metrics

def main():
    # Parameters
    ticker = 'TCS.NS'
    start_date = '2020-01-01'
    end_date = '2023-01-01'
    
    # Data Collection
    data = get_data(ticker, start_date, end_date)
    
    # Exploratory Data Analysis
    plot_closing_prices(data, ticker)
    
    # Feature Engineering
    data = add_moving_averages(data)
    
    # Strategy Implementation
    data = generate_signals(data)
    
    # Backtesting
    data = backtest_strategy(data)
    plot_returns(data)
    
    # Performance Metrics
    calculate_metrics(data)

if __name__ == "__main__":
    main()
