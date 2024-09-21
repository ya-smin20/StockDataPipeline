from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URI = os.getenv('DATABASE_URI')

def load_data():
    try:
       
        df = pd.read_csv('data/processed_stock_data.csv')
        
        
        engine = create_engine(DATABASE_URI , echo=False)
        
        conn = engine.connect()
        
        df.to_sql('stock_data', conn, if_exists='replace', index=False)
        
        print("Data loaded successfully into PostgreSQL.")
    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    load_data()
