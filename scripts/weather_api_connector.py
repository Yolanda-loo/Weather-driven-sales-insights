import requests
import pandas as pd
from datetime import datetime

API_KEY = "YOUR_API_KEY"
CITY = "Johannesburg"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

# Extract relevant fields
weather_data = {
    "Date": datetime.now().strftime('%Y-%m-%d'),
    "Temperature": data['main']['temp'],
    "Humidity": data['main']['humidity'],
    "Condition": data['weather'][0]['main']
}

# Save to CSV
df = pd.DataFrame([weather_data])

file_path = "../data/weather_data.csv"

try:
    existing = pd.read_csv(file_path)
    df = pd.concat([existing, df], ignore_index=True)
except:
    pass

df.to_csv(file_path, index=False)

print("✅ Weather data collected!")
