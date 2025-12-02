from collector import fetch_crypto_data
from preprocessor import preprocess_data
from trainer import train_model
from predictor import predict_next_price

import os

CRYPTOS = {
    "Bitcoin": "BTC-USD",
    "Ethereum": "ETH-USD",
    "Ripple": "XRP-USD",
    "Litecoin": "LTC-USD",
    "Cardano": "ADA-USD"
}

def run_crypto_agent():
    print("\n Starting Crypto AI Predictor Agent...\n")

    os.makedirs("data", exist_ok=True)
    os.makedirs("models", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    for name, symbol in CRYPTOS.items():
        print(f"\n==========={name}===========")

        # fetch data
        print(f"\n Fetching data for {name} ({symbol})...")
        raw_path = fetch_crypto_data()

        # preprocess data
        print(f"\n Preprocessing data for {name}...")

        # train model
        model_path = f"models/{name.lower()}_model.pkl"
        print(f"\n Training model for {name}...")
        train_model(raw_path, model_path)

        # predict next price
        print(f"\n Predicting next price for {name}...")
        predict_next_price(raw_path, model_path, name)

    print("\n Crypto AI Predictor Agent completed all tasks.\n")

if __name__ == "__main__":
    run_crypto_agent()