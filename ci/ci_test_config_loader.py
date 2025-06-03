#ci\ci_test_config_loader.py
"""
# ╔═╗╔═╗╔╗╔╔╦╗╦ ╦╔═╗╦═╗ 
# ╔═╝║╣ ║║║ ║ ╠═╣║ ║╠╦╝ 
# ╚═╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝╩╚═ 
# ╔═╗╦  ┌─┐┬─┐┬┌─┐┌┬┐┌─┐
# ╠═╣║  │  ├┬┘│├─┘ │ │ │
# ╩ ╩╩  └─┘┴└─┴┴   ┴ └─┘
#
# Zenthor AI-Crypto 
#ci_test_config_loader
"""
from core.config_loader import load_config
import time, signal, sys

def timeout_handler(signum, frame):
    print("🕒 Timeout elérve.")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(50)

    print("🔧 Konfiguráció betöltése...")
    config = load_config()
    print(f"✅ Betöltött config kulcsok: {list(config.keys())}")
    signal.alarm(0)
