import csv
import json
import urllib.request
from datetime import datetime
import os

def fetch_crypto_prices(coin_ids):
    # Using CoinGecko API v3
    ids = ','.join(coin_ids)
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd'
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        print(f"Error fetching prices: {e}")
        return None

def load_portfolio(filename):
    portfolio = []
    coin_ids = set()
    
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                portfolio.append({
                    'memo': row['memo'],
                    'coin_id': row['coin_id'],
                    'quantity': float(row['quantity'])
                })
                coin_ids.add(row['coin_id'])
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None, None
    
    return portfolio, list(coin_ids)

def log_portfolio_value(value):
    log_file = 'portfolio_history.csv'
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Check if file exists and create with headers if it doesn't
    if not os.path.exists(log_file):
        with open(log_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'total_value'])
    
    # Append new log entry
    try:
        with open(log_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_date, f"{value:.2f}"])
    except Exception as e:
        print(f"Error writing to log file: {e}")

def main():
    # Load portfolio from CSV
    portfolio, coin_ids = load_portfolio('portfolio.csv')
    if not portfolio:
        return
    
    # Fetch current prices
    prices = fetch_crypto_prices(coin_ids)
    if not prices:
        return
    
    # Calculate and display portfolio
    total_value = 0
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print("\nCrypto Portfolio Valuation")
    print(f"Time: {current_time}")
    print("\n{:<20} {:<10} {:<12} {:<12} {:<15}".format(
        "Memo", "Coin", "Quantity", "Price (USD)", "Value (USD)"))
    print("-" * 70)
    
    for item in portfolio:
        coin_id = item['coin_id']
        quantity = item['quantity']
        price = prices[coin_id]['usd']
        value = quantity * price
        total_value += value
        
        print("{:<20} {:<10} {:<12.4f} ${:<11.2f} ${:<14.2f}".format(
            item['memo'][:20],
            coin_id[:10],
            quantity,
            price,
            value
        ))
    
    print("-" * 70)
    print("{:<45} ${:<14.2f}".format("Total Portfolio Value:", total_value))
    
    # Log the total portfolio value
    log_portfolio_value(total_value)
    print(f"\nPortfolio value logged to portfolio_history.csv")

if __name__ == "__main__":
    main()