# cell 1
import requests
import pandas as pd
import matplotlib.pyplot as plt

# cell 2
key = "YOUR_API_KEY"
city = "Pune"
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&units=metric"

# cell 3
data = requests.get(url).json()

# cell 4
df = pd.DataFrame([{
    "Date": x["dt_txt"],
    "Temperature": x["main"]["temp"],
    "Humidity": x["main"]["humidity"],
    "Wind": x["wind"]["speed"]
} for x in data["list"]])

# cell 5
print(df.head())
print("Average Temperature:", df["Temperature"].mean())
print("Maximum Temperature:", df["Temperature"].max())
print("Minimum Temperature:", df["Temperature"].min())

# cell 6
df.plot(x="Date", y="Temperature", kind="line", title="Temperature Forecast")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# cell 7
df.plot(x="Date", y="Humidity", kind="bar", title="Humidity Forecast")
plt.tight_layout()
plt.show()

# cell 8
df.plot(x="Temperature", y="Humidity", kind="scatter", title="Temperature vs Humidity")
plt.show()

# cell 9
# Save to HTML file
import folium

city_coord = [data["city"]["coord"]["lat"], data["city"]["coord"]["lon"]]
m = folium.Map(location=city_coord)
folium.Marker(city_coord, popup=city).add_to(m)
m.save("weather_map.html")

df.to_html("weather_data.html", index=False)
print("Saved to weather_map.html and weather_data.html")