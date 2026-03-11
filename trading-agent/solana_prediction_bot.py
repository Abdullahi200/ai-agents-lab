import requests
import time
import numpy as np

URL = "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT"

prices = []

def get_price():
    r = requests.get(URL)
    return float(r.json()["price"])

while True:
    price = get_price()
    prices.append(price)

    if len(prices) > 20:
        prices.pop(0)

        avg = np.mean(prices)

        if price > avg:
            print("Prediction: UP")
        else:
            print("Prediction: DOWN")

    print("Price:", price)

    time.sleep(5)
