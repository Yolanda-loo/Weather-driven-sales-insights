import pandas as pd

# Step 1: Load datasets
sales_df = pd.read_csv("data/sales_data.csv")         # Example columns: Date, Region, Product, Revenue, Expenses, Customers
weather_df = pd.read_csv("data/weather_data.csv")     # Example columns: Timestamp, City, Temperature, Humidity, Pressure, Weather

# Step 2: Convert date formats
sales_df["Date"] = pd.to_datetime(sales_df["Date"])
weather_df["Timestamp"] = pd.to_datetime(weather_df["Timestamp"])

# Step 3: Align by date (merge on closest timestamp)
# Extract just the date from weather timestamp
weather_df["Date"] = weather_df["Timestamp"].dt.date
sales_df["Date"] = sales_df["Date"].dt.date

# Step 4: Merge datasets
merged_df = pd.merge(sales_df, weather_df, on="Date", how="left")

# Step 5: Save merged dataset
merged_df.to_csv("data/sales_weather_merged.csv", index=False)

print("Merged dataset created: data/sales_weather_merged.csv")
print(merged_df.head())
