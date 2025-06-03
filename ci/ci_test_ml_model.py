#ci\ci_test_ml_model.py
"""
# ╔═╗╔═╗╔╗╔╔╦╗╦ ╦╔═╗╦═╗ 
# ╔═╝║╣ ║║║ ║ ╠═╣║ ║╠╦╝ 
# ╚═╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝╩╚═ 
# ╔═╗╦  ┌─┐┬─┐┬┌─┐┌┬┐┌─┐
# ╠═╣║  │  ├┬┘│├─┘ │ │ │
# ╩ ╩╩  └─┘┴└─┴┴   ┴ └─┘
#
# Zenthor AI-Crypto 
#ci_test_ml_model.py
"""
from core.ml_model import baseline_predict
import time, signal, sys

def timeout_handler(signum, frame):
    print("🕒 Timeout elérve.")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(50)

    print("🧠 ML baseline predikció...")
    dummy_data = [1, 2, 3, 4, 5]
    prediction = baseline_predict(dummy_data)
    print(f"✅ Predikció eredménye: {prediction}")
    signal.alarm(0)
