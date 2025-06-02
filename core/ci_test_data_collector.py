# ci_test_data_collector.py

from core.data_collector import fetch_price

if __name__ == "__main__":
    symbol = "BTC/USDT"
    price = fetch_price(symbol)
    print(f"✅ {symbol} aktuális ára: {price:.2f} USD")
