import streamlit as st
import pandas as pd

def load_data():
    stock_df = pd.read_csv('data/processed_stock_data.csv')
    news_df = pd.read_csv('data/financial_news.csv')
    return stock_df, news_df

def main():
    st.title('Stock Market Dashboard')

    stock_df, news_df = load_data()

    st.header('Stock Data')
    st.line_chart(stock_df[['date', 'moving_average_20']].set_index('date'))

    st.header('Financial News')
    st.dataframe(news_df)

if __name__ == "__main__":
    main()
