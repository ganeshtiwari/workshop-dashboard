import os 
import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
import plotly.graph_objects as go
from dotenv import load_dotenv

st.set_page_config(page_title="IBM Stock Dashboard", layout="wide")
load_dotenv()

@st.cache_resource
def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "postgres"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=int(os.getenv("POSTGRES_PORT", 5432))
    )

def fetch_stock_data(symbol):
    conn = get_connection()
    query = f"SELECT * FROM stock_prices WHERE symbol = '{symbol}' ORDER BY trading_date ASC"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Load data
df = fetch_stock_data("IBM")
df["trading_date"] = pd.to_datetime(df["trading_date"])

st.title("📈 IBM Monthly Stock Analysis")

# Sidebar Filters
st.sidebar.header("🔎 Filter Options")
date_range = st.sidebar.date_input("Select Date Range", [df["trading_date"].min(), df["trading_date"].max()])
df_filtered = df[(df["trading_date"] >= pd.to_datetime(date_range[0])) & (df["trading_date"] <= pd.to_datetime(date_range[1]))]

# Candlestick Chart
st.subheader("🕯️ Candlestick Chart")
fig = go.Figure(data=[go.Candlestick(
    x=df_filtered["trading_date"],
    open=df_filtered["open"],
    high=df_filtered["high"],
    low=df_filtered["low"],
    close=df_filtered["close"],
    increasing_line_color="green",
    decreasing_line_color="red"
)])
fig.update_layout(title="IBM Candlestick Chart", xaxis_title="Date", yaxis_title="Stock Price (USD)")
st.plotly_chart(fig, use_container_width=True)

# tock Prices with Moving Averages
st.subheader("📊 Stock Prices with Moving Averages")
df_filtered["50_MA"] = df_filtered["close"].rolling(window=50).mean()
df_filtered["200_MA"] = df_filtered["close"].rolling(window=200).mean()

fig = px.line(df_filtered, x="trading_date", y=["close", "50_MA", "200_MA"], labels={"value": "Price (USD)"})
fig.update_layout(title="IBM Stock Price & Moving Averages", xaxis_title="Date", yaxis_title="Price (USD)")
st.plotly_chart(fig, use_container_width=True)

# Volume vs. Stock Price
st.subheader("📊 Volume vs. Stock Price")
fig = px.scatter(df_filtered, x="volume", y="close", trendline="ols", title="IBM Stock Price vs. Volume")
st.plotly_chart(fig, use_container_width=True)

# Dividend Payouts
st.subheader("💰 Dividend Payouts Over Time")
fig = px.bar(df_filtered, x="trading_date", y="dividend_amount", title="IBM Dividend Payouts")
st.plotly_chart(fig, use_container_width=True)

# Show Data
st.subheader("📜 Data Preview")
st.dataframe(df_filtered.tail())
