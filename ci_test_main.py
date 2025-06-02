# ╔═╗╔═╗╔╗╔╔╦╗╦ ╦╔═╗╦═╗ 
# ╔═╝║╣ ║║║ ║ ╠═╣║ ║╠╦╝ 
# ╚═╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝╩╚═ 
# ╔═╗╦  ┌─┐┬─┐┬┌─┐┌┬┐┌─┐
# ╠═╣║  │  ├┬┘│├─┘ │ │ │
# ╩ ╩╩  └─┘┴└─┴┴   ┴ └─┘
# ┌┬┐┌─┐┬┌┐┌ ┌─┐┬ ┬     
# │││├─┤││││ ├─┘└┬┘     
# ┴ ┴┴ ┴┴┘└┘o┴   ┴  

# main.py
# main.py – Egyszerű HTTP healthcheck a konténerhez

import signal
import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from core.config_loader import load_config

if __name__ == "__main__":
    config = load_config()
    print("✅ Config sikeresen betöltve:")
    print(config)


class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Zenthor AI-Crypto online.")

def start_http_server():
    server = HTTPServer(('', 8080), HealthCheckHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    print("✅ HealthCheck szerver elindult a 8080-as porton")

def shutdown_handler(signum, frame):
    print("🛑 Leállítási jel érkezett. Kilépés...")
    exit(0)

if __name__ == "__main__":
    config = load_config()
    start_http_server()
    signal.signal(signal.SIGTERM, shutdown_handler)
    signal.signal(signal.SIGINT, shutdown_handler)

    while True:
        time.sleep(60)
