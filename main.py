import signal
import time

print("Zenthor AI-Crypto is running!")

def shutdown_handler(signum, frame):
    print("Leállítási jel érkezett. Kilépés...")
    exit(0)

# Kapcsolódás a SIGTERM és SIGINT jelekhez (Docker stop és Ctrl+C)
signal.signal(signal.SIGTERM, shutdown_handler)
signal.signal(signal.SIGINT, shutdown_handler)

# Végtelen várakozás, de szabályos leállítási lehetőséggel
while True:
    time.sleep(60)
