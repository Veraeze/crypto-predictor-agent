import yfinance as yf
import os
from config import CRYPTO_ASSETS, START_DATE, END_DATE


def fetch_crypto_data():
    os.makedirs("data", exist_ok=True)

    for name, symbol in CRYPTO_ASSETS.items():
        print(f"\n Fetching data for {name} ({symbol})...")

        df = yf.download(symbol, start=START_DATE, end=END_DATE)

        if df.empty:
            print(f"No data found for {name}")
            continue

        file_path = f"data/{name.lower()}_historical.csv"
        df.to_csv(file_path)

        print(f"Data saved to {file_path}")
        return file_path

if __name__ == "__main__":
    fetch_crypto_data()