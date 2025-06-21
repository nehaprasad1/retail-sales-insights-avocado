

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data/avocado.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['month'] = df['Date'].dt.month

st.title(" Avocado Trend Analytics Dashboard")
st.markdown("Explore trends in avocado prices and sales across US regions.")

# Filters
region = st.selectbox("Select Region", sorted(df['region'].unique()))
year = st.selectbox("Select Year", sorted(df['year'].unique()))
type_ = st.radio("Select Type", df['type'].unique())

# Filtered data
filtered = df[(df['region'] == region) & (df['year'] == year) & (df['type'] == type_)]

# Plot
st.subheader(f"Average Price in {region} - {year} ({type_})")

avg_by_date = filtered.groupby('Date')['AveragePrice'].mean()

fig, ax = plt.subplots()
ax.plot(avg_by_date.index, avg_by_date.values, marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Average Price ($)")
ax.set_title("Price Trend")
ax.grid(True)

st.pyplot(fig)
