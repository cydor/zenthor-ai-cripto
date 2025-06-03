#ci_test_data_collector.py
"""
# ╔═╗╔═╗╔╗╔╔╦╗╦ ╦╔═╗╦═╗ 
# ╔═╝║╣ ║║║ ║ ╠═╣║ ║╠╦╝ 
# ╚═╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝╩╚═ 
# ╔═╗╦  ┌─┐┬─┐┬┌─┐┌┬┐┌─┐
# ╠═╣║  │  ├┬┘│├─┘ │ │ │
# ╩ ╩╩  └─┘┴└─┴┴   ┴ └─┘
#
# Zenthor AI-Crypto 
#ci_test_data_collector
"""

from core.data_collector import fetch_price
import time, signal, sys

def timeout_handler(signum, frame):
    print("🕒 Timeout elérve.")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(50)

    print("🚀 Árfolyam lekérés Binance-ról...")
    price = fetch_price("BTC/USDT")
    print(f"✅ BTC/USDT ára: {price:.2f} USD")
    signal.alarm(0)
