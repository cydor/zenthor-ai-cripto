# ci_test_data_collector.py
import time
import signal
import sys
from core.data_collector import fetch_price

def shutdown_handler(signum, frame):
    print("🛑 Leállítási jel érkezett. Kilépés...")
    sys.exit(0)

if __name__ == "__main__":
    symbol = "BTC/USDT"
    price = fetch_price(symbol)
    print(f"✅ {symbol} aktuális ára: {price:.2f} USD")

    # Leállítási jelek kezelése
    signal.signal(signal.SIGTERM, shutdown_handler)
    signal.signal(signal.SIGINT, shutdown_handler)

    # CI-n 50 másodperc után kilép
    print("⏳ Várakozás 50 másodpercig...")
    time.sleep(50)
    print("✅ CI tesztidő lejárt. Kilépés.")
