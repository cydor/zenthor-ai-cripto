#client_factory.py

from binance.client import Client
import os

def create_binance_client(env, api_key, api_secret):
    client = Client(api_key, api_secret)
    
    if env == 'testnet':
        client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
    return client
