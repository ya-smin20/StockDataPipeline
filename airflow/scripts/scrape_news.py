from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
from sqlalchemy import create_engine

load_dotenv()

URL = os.getenv('URL')
DATABASE_URI = os.getenv('DATABASE_URI')

def scrape_news():
    try:
        # Debugging: Checking the response status
        response = requests.get(URL)
        print(f"Response Status: {response.status_code}")
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from {URL}")

        soup = BeautifulSoup(response.text, 'html.parser')
        
        headlines = []
        dates = []
        
        # Debugging: Check if the page has the desired structure
        items = soup.find_all('li', class_='js-stream-item')
        print(f"Found {len(items)} news items.")

        for item in items:
            headline = item.find('h3')
            if headline:
                headlines.append(headline.get_text())
                date_tag = item.find('time')
                date = date_tag['datetime'] if date_tag else datetime.now().isoformat()
                dates.append(date)
        
        df = pd.DataFrame({
            'headline': headlines,
            'date': dates
        })

        # Debugging: Check the DataFrame contents
        print("DataFrame head:")
        print(df.head())

        # Save scraped data to PostgreSQL
        engine = create_engine(DATABASE_URI)
        try:
            # Debugging: Check engine connection before loading data
            print(f"Engine Connection: {engine}")
            df.to_sql('financial_news', engine, if_exists='replace', index=False)
            print("Financial news data loaded successfully.")
        except Exception as e:
            print(f"Error loading news data: {e}")
    except Exception as scrape_error:
        print(f"Scraping failed: {scrape_error}")

if __name__ == "__main__":
    scrape_news()
