import matplotlib.pyplot as plt
import pandas as pd

# analysis/plots.py

import matplotlib.pyplot as plt
import pandas as pd

def plot_avg_price_by_month(df):
    df['month'] = df['Date'].dt.month
    monthly_avg = df.groupby('month')['AveragePrice'].mean()

    plt.figure(figsize=(8, 5))
    plt.plot(monthly_avg.index, monthly_avg.values, marker='o', color='green')
    plt.title('Average Avocado Price by Month')
    plt.xlabel('Month')
    plt.ylabel('Average Price ($)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_top_regions(df):
    region_avg = df.groupby('region')['AveragePrice'].mean().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10, 5))
    region_avg.plot(kind='bar', color='orange')
    plt.title('Top 10 Regions by Average Avocado Price')
    plt.xlabel('Region')
    plt.ylabel('Average Price ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_price_trend_by_type(df):
    df['Date'] = pd.to_datetime(df['Date'])
    avg_by_date_type = df.groupby(['Date', 'type'])['AveragePrice'].mean().unstack()

    avg_by_date_type.plot(figsize=(12, 6), title="Average Avocado Price Over Time by Type")
    plt.xlabel('Date')
    plt.ylabel('Average Price ($)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_volume_vs_price(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Total Volume'], df['AveragePrice'], alpha=0.3, color='purple')
    plt.title('Total Volume vs Average Price')
    plt.xlabel('Total Volume')
    plt.ylabel('Average Price')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_top_regions_by_volume(df):
    region_volume = df.groupby('region')['Total Volume'].sum().sort_values(ascending=False).head(10)
    region_volume.plot(kind='bar', figsize=(10, 5), color='teal')
    plt.title('Top 10 Regions by Total Avocado Sales Volume')
    plt.ylabel('Total Volume')
    plt.xlabel('Region')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

