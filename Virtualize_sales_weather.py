import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load merged dataset
df = pd.read_csv("data/sales_weather_merged.csv")

# Step 2: Scatter plot - Revenue vs Temperature
plt.figure(figsize=(8,6))
sns.scatterplot(x="Temperature", y="Revenue", data=df, hue="Region", palette="coolwarm")
plt.title("Revenue vs Temperature by Region")
plt.xlabel("Temperature (°C)")
plt.ylabel("Revenue")
plt.legend(title="Region")
plt.tight_layout()
plt.show()

# Step 3: Line chart - Average Revenue on Rainy vs Sunny Days
df["WeatherType"] = df["Weather"].apply(lambda x: "Rainy" if "rain" in str(x).lower() else "Sunny")
avg_revenue = df.groupby(["Date","WeatherType"])["Revenue"].mean().reset_index()

plt.figure(figsize=(10,6))
sns.lineplot(x="Date", y="Revenue", hue="WeatherType", data=avg_revenue, marker="o")
plt.title("Revenue Trends: Rainy vs Sunny Days")
plt.xlabel("Date")
plt.ylabel("Average Revenue")
plt.legend(title="Weather Type")
plt.tight_layout()
plt.show()

# Step 4: Bar chart - Profit by Weather Condition
df["Profit"] = df["Revenue"] - df["Expenses"]
profit_by_weather = df.groupby("Weather")["Profit"].mean().sort_values()

plt.figure(figsize=(10,6))
profit_by_weather.plot(kind="bar", color="skyblue")
plt.title("Average Profit by Weather Condition")
plt.xlabel("Weather Condition")
plt.ylabel("Average Profit")
plt.tight_layout()
plt.show()
