import requests
import pandas as pd
import datetime

# Replace with your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"
CITY = "Johannesburg"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather():
    """Fetch current weather data from OpenWeatherMap API."""
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "City": CITY,
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Pressure": data["main"]["pressure"],
            "Weather": data["weather"][0]["description"]
        }
        return weather_info
    else:
        print("Error fetching weather data:", response.status_code)
        return None

# Fetch and save weather data
weather_data = fetch_weather()
if weather_data:
    df = pd.DataFrame([weather_data])
    df.to_csv("data/weather_data.csv", mode="a", header=not pd.io.common.file_exists("data/weather_data.csv"), index=False)
    print("Weather data saved:", weather_data)
