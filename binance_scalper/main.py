# binance_scalper/main.py – Binance Futures tesztüzem

from core.config_loader import load_config
from client_factory import create_binance_client
from trade_engine import open_long_position, close_long_position

config = load_config()

api_key = config["binance_api_key"]
api_secret = config["binance_api_secret"]
env = config["env"]
symbol = config.get("symbol", "BTCUSDT")
quantity = config.get("trade_quantity", 0.001)

if not api_key or not api_secret:
    print("❌ API kulcs hiányzik, kilépés...")
    exit(1)

client = create_binance_client(env, api_key, api_secret)

# Pozíció nyitás
open_long_position(client, symbol, quantity)

input("Nyomj Entert a záráshoz...")

# Pozíció zárás
close_long_position(client, symbol, quantity)
