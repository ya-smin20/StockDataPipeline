from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

import sys
import os

#sys.path.append('/airflow/scripts') 
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))


from scripts.fetch_data import fetch_data
from scripts.process_data import process_data
from scripts.load_data import load_data
from scripts.scrape_news import scrape_news

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG('stock_etl_pipeline', default_args=default_args, schedule_interval='@daily') as dag:

    
    fetch_data_task = PythonOperator(
        task_id='fetch_data',
        python_callable=fetch_data
    )

    process_data_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data
    )

    load_data_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    scrape_news_task = PythonOperator(
        task_id='scrape_news',
        python_callable=scrape_news
    )

    
    fetch_data_task >> process_data_task >> load_data_task