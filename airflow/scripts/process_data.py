import pandas as pd

def process_data():
    df = pd.read_csv('data/stock_data.csv')
    df['moving_average_20'] = df['close'].rolling(window=20).mean()
    df.fillna(0, inplace=True)
    df.to_csv('data/processed_stock_data.csv', index=False)

if __name__ == "__main__":
    process_data()
