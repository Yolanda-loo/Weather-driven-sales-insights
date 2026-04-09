# 🌍 Weather-Driven Sales Insights

![Status](https://img.shields.io/badge/Project-Active-brightgreen)
![Tool](https://img.shields.io/badge/Python-API%20Integration%20%7C%20Pandas%20%7C%20Matplotlib-blue)
![Focus](https://img.shields.io/badge/Domain-Data%20Enrichment%20%7C%20Business%20Analysis-orange)

## 🚀 Objective
Integrate external **weather data** with sales records to analyze how environmental factors (temperature, rainfall, humidity) influence customer behavior and business performance.  
This project demonstrates your ability to combine **API integration, relational data engineering, and visualization** into actionable business insights.

---

## 🛠️ Workflow
1. **Weather Data Collection**  
   - `weather_api_connector.py` fetches live weather data from OpenWeatherMap API.  
   - Stores results in `weather_data.csv` with timestamps.

2. **Data Merging**  
   - `merge_sales_weather.py` joins sales records with weather data by date.  
   - Produces `sales_weather_merged.csv` for analysis.

3. **Visualization**  
   - `visualize_sales_weather.py` generates charts:  
     - Scatter plot: Revenue vs Temperature.  
     - Line chart: Revenue trends on Rainy vs Sunny days.  
     - Bar chart: Profit by weather condition.

4. **Insights**  
   - Identify correlations between weather and sales performance.  
   - Provide recommendations for marketing and inventory strategies.

---

## 📂 Deliverables
- `/data` → Sales dataset, weather dataset, merged dataset.  
- `/scripts` → API connector, merge script, visualization script.  
- `/database` → SQLite schema for storing combined records (optional).  
- `/visuals` → Charts showing weather impact on sales.  
- `/insights` → Markdown file summarizing findings and recommendations.  
- `README.md` → Documentation (this file).  

---

## 🔍 Business Value
- **Customer Behavior** → Understand how weather influences purchasing decisions.  
- **Marketing Strategy** → Target promotions based on seasonal/weather conditions.  
- **Operational Planning** → Adjust inventory and staffing for weather-driven demand.  

---

## 📸 Example Visualizations
*(Insert scatter plot, line chart, and bar chart screenshots here)*

---

## 🧭 Next Steps
- Expand to multi-city analysis for regional comparisons.  
- Add predictive modeling (e.g., regression to forecast sales based on weather).  
- Deploy pipeline to cloud (Azure Data Factory + Power BI integration).
