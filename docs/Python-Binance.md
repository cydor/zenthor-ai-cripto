 Pozíciónyitás/Zárás Binance Futures Testneten – Python-Binance
Feltétel: python-binance telepítve legyen
(Ha nincs: pip install python-binance)

1. Client inicializálása Testnethez
python
Másolás
Szerkesztés
from binance.client import Client

API_KEY = 'A_TE_TESTNET_API_KULCSOD'
API_SECRET = 'A_TE_TESTNET_API_TITKOD'

client = Client(API_KEY, API_SECRET)

# FONTOS: Futures testnet URL beállítása
client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
2. Pozíció nyitása LONG irányban (USDT-M Futures)
python
Másolás
Szerkesztés
order = client.futures_create_order(
    symbol='BTCUSDT',
    side='BUY',
    type='MARKET',
    quantity=0.001
)
print(order)
3. Pozíció zárása (SHORT eladással)
python
Másolás
Szerkesztés
close_order = client.futures_create_order(
    symbol='BTCUSDT',
    side='SELL',
    type='MARKET',
    quantity=0.001
)
print(close_order)
⚠️ Ügyelj a quantity értékre: ez mindig a coin mennyiségét jelenti (pl. 0.001 BTC), nem USDT-t.

🔐 API-kulcsok kezelése (Tesztelés vs Éles)
🔸 Fejlesztési fázisban:
Használj .env fájlt vagy config.yaml-t a kulcsok kezelésére.

Például .env fájl:

ini
Másolás
Szerkesztés
API_KEY_TESTNET=xxxxx
API_SECRET_TESTNET=yyyyy
Betöltés Pythonból:

python
Másolás
Szerkesztés
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY_TESTNET")
🔸 Ha más tesztelőnek adod:
Igen, minden tesztelőnek saját Binance Testnet fiókra és kulcsokra van szüksége.

Érdemes a rendszeredben egy kulcsbetöltő modult készíteni, amit a felhasználó .env-vel vagy UI-n keresztül tud konfigurálni.

🔁 Teszt és Éles rendszer közti váltás (és több tőzsde támogatása)
🔹 Javasolt struktúra:
plaintext
Másolás
Szerkesztés
config/
    binance_testnet.yaml
    binance_mainnet.yaml
    bybit_testnet.yaml
    ...
core/
    client_factory.py
    trade_engine.py
    strategy_scalping.py
main.py
🔸 Például client_factory.py:
python
Másolás
Szerkesztés
from binance.client import Client

def create_binance_client(env='testnet', api_key=None, api_secret=None):
    client = Client(api_key, api_secret)
    if env == 'testnet':
        client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
    return client
Így elegáns módon tudod:

váltani a környezeteket (testnet, mainnet)

később akár más tőzsdékhez is hasonló klienst írni (create_bybit_client, stb.)

bármelyik modult újraindítás nélkül átkapcsolni éles vagy tesztelésre

✅ Összefoglalás

Funkció	Ajánlás
Testnet hozzáférés	Minden tesztelő regisztráljon saját Binance Futures Testnet fiókot
API-kulcs kezelés	.env, yaml, GitHub Secrets, vagy UI-felületes megadás
Környezetek elkülönítése	client_factory-sémával, testnet/mainnet kapcsolóval
Több tőzsde támogatás	Ugyanez a struktúra új exchange_client.py-kkel bővíthető
