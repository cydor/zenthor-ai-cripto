# ci_test_data_collector.pyimport time

import signal
import sys

def shutdown_handler(signum, frame):
    print("🛑 Leállítási jel érkezett. Kilépés...")
    sys.exit(0)

if __name__ == "__main__":
    from core.exchange_connector import get_exchange
    from core.config_loader import load_config

    config = load_config()
    print("✅ Betöltött környezet:", config.get("env"))
    
    exchange = get_exchange("binance", config)
    print("📈 Exchange betöltve:", exchange)

    # CI futás limit – max 50 másodperc
    signal.signal(signal.SIGTERM, shutdown_handler)
    signal.signal(signal.SIGINT, shutdown_handler)
    print("⏳ Várakozás 50 másodpercig...")
    time.sleep(50)
    print("✅ CI tesztidő lejárt. Kilépés.")
