# core/exchange_connector.py

import ccxt
import os

import json

from core.config_loader import load_config

class ExchangeConnector:
    def __init__(self, config=None):
        self.config = config or load_config()
        self.exchanges = {}

        for ex_name in self.config.get("exchanges", []):
            self.exchanges[ex_name] = self._create_exchange(ex_name)

    def _create_exchange(self, name):
        name = name.lower()
        if name not in ccxt.exchanges:
            raise ValueError(f"❌ Ismeretlen tőzsde: {name}")

        if name == "binance":
            return ccxt.binance({
                'apiKey': self.config.get("binance_api_key", ""),
                'secret': self.config.get("binance_api_secret", ""),
                'enableRateLimit': True
            })

        # További tőzsdék inicializálása itt
        return getattr(ccxt, name)({'enableRateLimit': True})

    def get_price(self, symbol="BTC/USDT", exchange="binance"):
        exchange = exchange.lower()
        if exchange not in self.exchanges:
            raise ValueError(f"❌ A kért tőzsde nincs betöltve: {exchange}")
        ticker = self.exchanges[exchange].fetch_ticker(symbol)
        return ticker['last']
