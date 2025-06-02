# ╔═╗╔═╗╔╗╔╔╦╗╦ ╦╔═╗╦═╗ 
# ╔═╝║╣ ║║║ ║ ╠═╣║ ║╠╦╝ 
# ╚═╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝╩╚═ 
# ╔═╗╦  ┌─┐┬─┐┬┌─┐┌┬┐┌─┐
# ╠═╣║  │  ├┬┘│├─┘ │ │ │
# ╩ ╩╩  └─┘┴└─┴┴   ┴ └─┘
# ┌┬┐┌─┐┬┌┐┌ ┌─┐┬ ┬     
# │││├─┤││││ ├─┘└┬┘     
# ┴ ┴┴ ┴┴┘└┘o┴   ┴  

# ci_test_main.py
# A cél: ✅ Konfig betöltés → 📤 Kiírás → 🚪 Kilépés

import signal
import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from core.config_loader import load_config

if __name__ == "__main__":
    config = load_config()
    print("✅ Config sikeresen betöltve:")
    print(config)

