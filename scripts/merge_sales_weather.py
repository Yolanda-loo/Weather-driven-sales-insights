import pandas as pd

# Load datasets
sales = pd.read_csv('../data/sales_data.csv')
weather = pd.read_csv('../data/weather_data.csv')

# Convert dates
sales['Date'] = pd.to_datetime(sales['Date'])
weather['Date'] = pd.to_datetime(weather['Date'])

# Merge on Date
merged = pd.merge(sales, weather, on='Date', how='inner')

# Save merged dataset
merged.to_csv('../data/sales_weather_merged.csv', index=False)

print("✅ Data merged successfully!")
