
# Crypto Price Prediction Agent

## Project Overview
This project is an AI-powered Crypto Price Prediction Agent built with Python. It automates the process of collecting cryptocurrency data, preprocessing it, training machine learning models, and predicting the next-day closing price for multiple cryptocurrencies including Bitcoin, Ethereum, Litecoin, Ripple, and Cardano.

## Features
- Automated data collection from Yahoo Finance
- Data preprocessing and cleaning for time-series analysis
- Training of machine learning models (Linear Regression)
- Next-day price prediction for multiple cryptocurrencies
- Outputs predictions to CSV files in an organized structure
- Full pipeline can be run with a single command (`main.py`)

## Tools and Technologies
- Python 3
- pandas, numpy
- scikit-learn
- yfinance
- joblib
- matplotlib (optional for visualizations)

## Folder Structure
```
crypto_predictor/
│
├── data/             # Raw historical cryptocurrency CSV files
├── models/           # Trained ML models
├── output/           # Predicted next-day prices
├── collector.py      # Module for fetching cryptocurrency data
├── preprocessor.py   # Module for cleaning and preprocessing data
├── trainer.py        # Module for training ML models
├── predictor.py      # Module for generating predictions
├── main.py           # Runs the full pipeline
├── config.py         # Configuration for cryptocurrencies and date ranges
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

## How to Run
1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/crypto-price-prediction-agent.git
cd crypto-price-prediction-agent
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the full pipeline:

```bash
python main.py
```

5. Check the `output/` folder for predicted next-day prices.

## Example Output
```
Crypto,Next_Close_Price
Bitcoin,85237.48
Ethereum,3121.45
Litecoin,142.12
Ripple,0.85
Cardano,1.45
```

## Notes
- Ensure you have an active internet connection for data collection.
- Large files (models, CSV data) are excluded from GitHub via `.gitignore`.
- The pipeline is modular, allowing you to run data collection, training, or prediction independently if desired.
