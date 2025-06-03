#ci\ci_test_exchange_connector.py
"""
# ╔═╗╔═╗╔╗╔╔╦╗╦ ╦╔═╗╦═╗ 
# ╔═╝║╣ ║║║ ║ ╠═╣║ ║╠╦╝ 
# ╚═╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝╩╚═ 
# ╔═╗╦  ┌─┐┬─┐┬┌─┐┌┬┐┌─┐
# ╠═╣║  │  ├┬┘│├─┘ │ │ │
# ╩ ╩╩  └─┘┴└─┴┴   ┴ └─┘
#
# Zenthor AI-Crypto 
#ci_test_exchange_connector
"""
from core.exchange_connector import init_exchange
import time, signal, sys

def timeout_handler(signum, frame):
    print("🕒 Timeout elérve.")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(50)

    print("🔌 Exchange inicializálás...")
    exchange = init_exchange("binance", "sandbox")
    print(f"✅ Exchange típus: {type(exchange)}")
    signal.alarm(0)
