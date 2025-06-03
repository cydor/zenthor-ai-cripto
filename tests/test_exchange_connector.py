# test/test_exchange_connector.py
"""
# ╔═╗╔═╗╔╗╔╔╦╗╦ ╦╔═╗╦═╗ 
# ╔═╝║╣ ║║║ ║ ╠═╣║ ║╠╦╝ 
# ╚═╝╚═╝╝╚╝ ╩ ╩ ╩╚═╝╩╚═ 
# ╔═╗╦  ┌─┐┬─┐┬┌─┐┌┬┐┌─┐
# ╠═╣║  │  ├┬┘│├─┘ │ │ │
# ╩ ╩╩  └─┘┴└─┴┴   ┴ └─┘
#
# Zenthor AI-Crypto Dockerfile
"""


from core.exchange_connector import ExchangeConnector

def test_binance_price_fetch():
    connector = ExchangeConnector()
    price = connector.get_price("BTC/USDT", "binance")
    assert price > 0, f"Árfolyam nem pozitív: {price}"
    print(f"✅ Binance BTC/USDT ár: {price}")
