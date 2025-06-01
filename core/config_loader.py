import os
import json

def load_config():
    env = os.getenv("ENV", "dev")
    config_path = f"./config/{env}.json"

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"❌ Nincs ilyen konfigurációs fájl: {config_path}")

    if os.path.getsize(config_path) == 0:
        raise RuntimeError(f"⚠️ A konfigurációs fájl üres: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    print(f"✅ Betöltött környezet: {env}")
    return config
