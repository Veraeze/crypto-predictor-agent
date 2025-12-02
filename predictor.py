import pandas as pd
import joblib
import os
from preprocessor import preprocess_data

def predict_next_price(file_path, model_path, crypto_name):
    print(f"\n Predicting next price for {crypto_name}")

    df = preprocess_data(file_path)

    X_last = df[["Open", "High", "Low", "Close", "Volume"]].iloc[-1:].values

    model = joblib.load(model_path)
    next_price = model.predict(X_last)[0]

    os.makedirs("output", exist_ok=True)
    out_path = f"output/{crypto_name}_next_price.csv"
    pd.DataFrame({"Crypto": [crypto_name], "Next_Close_Price": [next_price]}).to_csv(out_path, index=False)

    print(f" Prediction complete! Next close price for {crypto_name}: {round(next_price,2)}")
    print(f" Saved to {out_path}")

    return next_price

if __name__ == "__main__":
    predict_next_price("data/bitcoin_historical.csv", "models/bitcoin_model.pkl", "Bitcoin")
    predict_next_price("data/ethereum_historical.csv", "models/ethereum_model.pkl", "Ethereum")
    predict_next_price("data/litecoin_historical.csv", "models/litecoin_model.pkl", "Litecoin")
    predict_next_price("data/ripple_historical.csv", "models/ripple_model.pkl", "Ripple")
    predict_next_price("data/cardano_historical.csv", "models/cardano_model.pkl", "Cardano")

