# data_collector.py – Binance demo adatlekérés
import ccxt
from core.config_loader import load_config

def collect_data():
    config = load_config()

    if not config["binance_api_key"] or not config["binance_api_secret"]:
        print("⚠️ Nincsenek beállítva API kulcsok – dummy mód?")
        return

    exchange = ccxt.binance({
        'apiKey': config["binance_api_key"],
        'secret': config["binance_api_secret"],
        'enableRateLimit': True,
        'options': {
            'defaultType': 'spot',
        }
    })

    try:
        ticker = exchange.fetch_ticker('BTC/USDT')
        print(f"📈 BTC/USDT árfolyam: {ticker['last']} USD")
    except Exception as e:
        print(f"❌ API hiba: {e}")

if __name__ == "__main__":
    collect_data()
