import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
SYMBOL = 'AAPL'
URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={SYMBOL}&apikey={API_KEY}'

def fetch_data():
    response = requests.get(URL)
    data = response.json()

    if 'Time Series (Daily)' in data:
        df = pd.DataFrame(data['Time Series (Daily)']).T
        df.index = pd.to_datetime(df.index)
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        df.reset_index(inplace=True)
        df.rename(columns={'index': 'date'}, inplace=True)
        df.to_csv('data/stock_data.csv', index=False)
        print("Data fetched and saved to data/stock_data.csv")
    else:
        print("Error fetching data:", data.get("Error Message", "Unknown error"))

if __name__ == "__main__":
    fetch_data()