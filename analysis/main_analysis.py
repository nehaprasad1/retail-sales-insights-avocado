import pandas as pd
from plots import plot_avg_price_by_month, plot_top_regions,plot_price_trend_by_type,plot_volume_vs_price, plot_top_regions_by_volume
#lpading the data
df = pd.read_csv('data/avocado.csv')
'''
#Data preview
print("first few rows of avacado data:")
print(df.head())

print("\n Data info: ")
print(df.info())

print("\n summary statistics: ")
print(df.describe())

print("\n column names: ")
print(df.columns.tolist())
'''
# data cleaning

#drop unnecessary index columns
df = df.drop(columns=['Unnamed: 0'])  # Correct


# type conversion
df['Date']=pd.to_datetime(df['Date'])

# removing extra space
df['region'] = df['region'].str.strip()

# remove duplicates
df=df.drop_duplicates()

#print(df.info())
# 1. Extract month and day from the date
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
threshold = df['AveragePrice'].quantile(0.75)
df['is_expensive'] = df['AveragePrice'] > threshold


# 3. Bucket Total Volume into low, medium, high categories
df['Total Volume'].describe()

df['volume_level'] = pd.cut(
    df['Total Volume'],
    bins = [0, 10000, 130000, df['Total Volume'].max()],

    labels=['Low', 'Medium', 'High']
)

#What is the average price per region?
region_avg_price = df.groupby('region')['AveragePrice'].mean().sort_values(ascending=False)
print(region_avg_price.head(10))


#What’s the total volume sold each year?
volume_by_year = df.groupby('year')['Total Volume'].sum()
print(volume_by_year)

# What’s the monthly price trend?
monthly_avg = df.groupby('month')['AveragePrice'].mean()
print(monthly_avg)

# Load the cleaned data
df = pd.read_csv('data/avocado.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Call your plotting functions
plot_avg_price_by_month(df)
plot_top_regions(df)
plot_price_trend_by_type(df)
plot_volume_vs_price(df)
plot_top_regions_by_volume(df)