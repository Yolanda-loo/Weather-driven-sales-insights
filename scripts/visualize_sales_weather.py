import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load merged data
df = pd.read_csv('../data/sales_weather_merged.csv')

# ----------------------------
# Scatter: Revenue vs Temperature
# ----------------------------
plt.figure()
sns.scatterplot(data=df, x='Temperature', y='Revenue')
plt.title("Revenue vs Temperature")
plt.savefig('../visuals/revenue_vs_temperature.png')

# ----------------------------
# Line: Revenue by Condition
# ----------------------------
df['Date'] = pd.to_datetime(df['Date'])

plt.figure()
for cond in df['Condition'].unique():
    subset = df[df['Condition'] == cond]
    plt.plot(subset['Date'], subset['Revenue'], label=cond)

plt.legend()
plt.title("Revenue Trends by Weather Condition")
plt.savefig('../visuals/revenue_by_weather.png')

# ----------------------------
# Bar: Profit by Weather Condition
# ----------------------------
plt.figure()
df.groupby('Condition')['Profit'].mean().plot(kind='bar')
plt.title("Average Profit by Weather Condition")
plt.savefig('../visuals/profit_by_weather.png')

print("✅ Visualizations created!")
``
