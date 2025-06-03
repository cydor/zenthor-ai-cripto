#ci\ci_test_indicators.py
"""
# ╔═╗╔═╗╔╗╔╔╦╗╦ ╦╔═╗╦═╗ 
# ╔═╝║╣ ║║║ ║ ╠═╣║ ║╠╦╝ 
# ╚═╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝╩╚═ 
# ╔═╗╦  ┌─┐┬─┐┬┌─┐┌┬┐┌─┐
# ╠═╣║  │  ├┬┘│├─┘ │ │ │
# ╩ ╩╩  └─┘┴└─┴┴   ┴ └─┘
#
# Zenthor AI-Crypto 
#ci_test_indicators
"""
from core.indicators import calculate_rsi
import pandas as pd
import time, signal, sys

def timeout_handler(signum, frame):
    print("🕒 Timeout elérve.")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(50)

    print("📈 RSI számítás dummy adaton...")
    df = pd.DataFrame({'close': [1, 2, 3, 4, 3, 2, 4, 5, 6, 4, 3, 2, 5, 6, 7, 8, 9]})
    rsi = calculate_rsi(df)
    print(f"✅ RSI: {rsi.dropna().values[-1]:.2f}")
    signal.alarm(0)
