import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("cleaned_sales.csv")

st.set_page_config(page_title="Retail Analytics", layout="wide")

st.title("📊 AI Retail Analytics Dashboard")

# ---- KPI Section ----
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df.shape[0]

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"{total_sales:,.0f}")
col2.metric("Total Profit", f"{total_profit:,.0f}")
col3.metric("Total Orders", total_orders)

# ---- Filter ----
region = st.selectbox("Select Region", df['Region'].unique())

filtered_df = df[df['Region'] == region]

# ---- Charts ----
st.subheader("Sales by Category")
st.bar_chart(filtered_df.groupby('Category')['Sales'].sum())

st.subheader("Monthly Sales Trend")
st.line_chart(filtered_df.groupby('Month')['Sales'].sum())

# ---- Top Products ----
st.subheader("Top Products")
top_products = filtered_df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)
st.bar_chart(top_products)