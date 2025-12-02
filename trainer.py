import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
from preprocessor import preprocess_data

def train_model(file_path, model_name="crypto_model.pkl"):
    print(f"Training model using {file_path}")

    df = preprocess_data(file_path)

    # predict tomorrow's Close using todays values
    df["Target"] = df["Close"].shift(-1)

    df = df.dropna()

    X = df[["Open", "High", "Low", "Close", "Volume"]]
    y = df["Target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    joblib.dump(model, model_name)

    print(f"Model trained and saved to models/{model_name}")
    print(f" Model accuracy (R² score): {round(accuracy, 4)}")

    return model

if __name__ == "__main__":
    train_model("data/bitcoin_historical.csv", "models/bitcoin_model.pkl")
    train_model("data/ethereum_historical.csv", "models/ethereum_model.pkl")
    train_model("data/litecoin_historical.csv", "models/litecoin_model.pkl")
    train_model("data/ripple_historical.csv", "models/ripple_model.pkl")
    train_model("data/cardano_historical.csv", "models/cardano_model.pkl")
