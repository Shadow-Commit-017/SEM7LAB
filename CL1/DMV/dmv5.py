# cell 1
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("City_Air_Quality.csv")
df["Date"] = pd.to_datetime(df["Date"])

print(df.head())
df.info()
print("Missing Values:")
print(df.isnull().sum())
print("\nSummary:")
print(df[["PM2.5", "PM10", "CO", "AQI"]].describe())

# cell 2
# AQI trend
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["AQI"], color="red")
plt.title("AQI Trend")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# cell 3
# Separate pollutant trends
for col in ["PM2.5", "PM10", "CO"]:
    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df[col])
    plt.title(col + " Trend")
    plt.xlabel("Date")
    plt.ylabel(col)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# cell 4
# Average AQI by month
df["Month"] = df["Date"].dt.to_period("M").astype(str)
monthly = df.groupby("Month")["AQI"].mean()
print(monthly)

monthly.plot(kind="bar", figsize=(8, 5))
plt.title("Average AQI by Month")
plt.xlabel("Month")
plt.ylabel("Average AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# cell 5
# AQI distribution by relative PM2.5 level
df["PM25Group"] = pd.qcut(df["PM2.5"], q=3, labels=["Lower third", "Middle third", "Upper third"])
print(df.groupby("PM25Group", observed=True)["AQI"].agg(["count", "mean"]))
df.boxplot(column="AQI", by="PM25Group", figsize=(8, 5))
plt.title("AQI by PM2.5 Level")
plt.suptitle("")
plt.xlabel("Relative PM2.5 Level")
plt.ylabel("AQI")
plt.tight_layout()
plt.show()

# cell 6
# Relationship between PM2.5 and AQI
plt.figure(figsize=(7, 5))
plt.scatter(df["PM2.5"], df["AQI"])
plt.title("PM2.5 and AQI")
plt.xlabel("PM2.5 (µg/m³)")
plt.ylabel("AQI")
plt.tight_layout()
plt.show()