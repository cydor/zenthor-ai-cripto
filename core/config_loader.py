# config_loader.py
import os
import json

def load_config():
    env = os.getenv("ENV", "dev")  # Alapértelmezett környezet
    config_file = f"config.{env}.json"

    try:
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f)
    except FileNotFoundError:
        raise RuntimeError(f"Konfigurációs fájl nem található: {config_file}")
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Hibás JSON a fájlban: {config_file} → {str(e)}")

    return config

import os
import json

def load_config():
    env = os.getenv("ENV", "dev")  # alapértelmezett: dev
    config_path = f"./config/{env}.json"

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"❌ Nincs ilyen konfigurációs fájl: {config_path}")

    if os.path.getsize(config_path) == 0:
        raise RuntimeError(f"⚠️ A konfigurációs fájl üres: {config_path}")

    with open(config_path, "r") as f:
        config = json.load(f)

    print(f"✅ Betöltött környezet: {env}")
    return config
