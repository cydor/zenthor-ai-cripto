#trade_engine.py

def open_long_position(client, symbol, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side='BUY',
            type='MARKET',
            quantity=quantity
        )
        print("LONG nyitva:", order)
    except Exception as e:
        print("Hiba LONG nyitáskor:", e)


def close_long_position(client, symbol, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side='SELL',
            type='MARKET',
            quantity=quantity
        )
        print("LONG zárva:", order)
    except Exception as e:
        print("Hiba LONG záráskor:", e)
