import pandas as pd

def preprocess_data(file_path):
    print(f"\n Preprocessing data from {file_path}")

    df = pd.read_csv(file_path, skiprows=[1,2])
    print("\nDEBUG — Raw columns:", df.columns)
    df.rename(columns={"Price": "Date"}, inplace=True)
    # df.reset_index(inplace=True)
    # df.rename(columns={"index": "Date"}, inplace=True)

    # set date to datetime
    df["Date"] = pd.to_datetime(df["Date"])
    print("\nDEBUG — First 5 rows after Date conversion:")
    print(df.head())

    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]
    df = df.dropna()

    print(f"Preprocessed complete: {len(df)} rows ready")

    return df

if __name__ == "__main__":
    test_df = preprocess_data("data/bitcoin_historical.csv")
    print(test_df.head())