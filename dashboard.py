import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Crypto Price Prediction Dashboard", layout="wide")

st.title("Crypto Price Prediction Dashboard")
st.markdown("View historical cryptocurrency prices and next-day predictions.")

CRYPTOS = ["Bitcoin", "Ethereum", "Litecoin", "Ripple", "Cardano"]

crypto_choice = st.selectbox("Select a cryptocurrency:", CRYPTOS)

# Paths
data_path = f"data/{crypto_choice.lower()}_historical.csv"
prediction_path = f"output/{crypto_choice}_next_price.csv"

# check if file exists
if not os.path.exists(data_path):
    st.error(f"No historical data found for {crypto_choice}. Please run the agent first.")
elif not os.path.exists(prediction_path):
    st.error(f"No prediction found for {crypto_choice}. Please run the agent first.")
else:
    # load data
    df = pd.read_csv(data_path, skiprows=[1, 2 ])
    df.rename(columns={"Price": "Date"}, inplace=True)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    # display last 30 days
    st.subheader(f"Last 30 Days Historical Prices for {crypto_choice}")
    display_df = df.tail(30).reset_index(drop=True)
    st.dataframe(display_df)

    # plot close price
    st.subheader("Closing Price Over Time")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Date"], df["Close"], marker="o")
    ax.set_xlabel("Date")
    ax.set_ylabel("Close Price")
    ax.set_title(f"{crypto_choice} Closing Prices")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # show next-day prediction
    pred_df = pd.read_csv(prediction_path)
    next_price = pred_df["Next_Close_Price"].values[0]
    st.subheader("Next-Day Predicted Close Price")
    st.metric(label=f"{crypto_choice} Predicted Close Price", value=f"${next_price:,.2f}")