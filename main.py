from airflow.scripts.fetch_data import fetch_data
from airflow.scripts.process_data import process_data
from airflow.scripts.load_data import load_data
from airflow.scripts.scrape_news import scrape_news

def run_etl():
    print("Starting the ETL pipeline...")
    
    
    print("Fetching stock data...")
    fetch_data()
    
    
    print("Processing data...")
    process_data()
    
    
    print("Loading data...")
    load_data()
    
    
    
    
    print("ETL pipeline completed successfully!")

if __name__ == "__main__":
    run_etl()
