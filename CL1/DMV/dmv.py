# cell 1
#pip install openpyxl
import pandas as pd
import matplotlib.pyplot as plt

salesCSV = pd.read_csv("sales_data.csv")
salesJSON = pd.read_json("sales_data.json")
salesExcel = pd.read_excel("sales_data.xlsx")

for name, data in [("CSV", salesCSV), ("JSON", salesJSON), ("Excel", salesExcel)]:
    print(name, "Data:")
    print(data.head())
    data.info()

# cell 2
# Check missing values
print("Missing Values in CSV:")
print(salesCSV.isnull().sum())

print("\nMissing Values in JSON:")
print(salesJSON.isnull().sum())

print("\nMissing Values in Excel:")
print(salesExcel.isnull().sum())

# cell 3
# Remove missing values and duplicates, then convert dates
def cleaning_data(data):
    data.dropna(inplace=True)
    data["Date"] = pd.to_datetime(data["Date"])
    data.drop_duplicates(inplace=True)
    return data

for data in [salesCSV, salesJSON, salesExcel]:
    cleaning_data(data)

# cell 4
# Combine file formats and count each order once
salesCSV["source"] = "CSV"
salesJSON["source"] = "JSON"
salesExcel["source"] = "Excel"

df = pd.concat([salesCSV, salesExcel, salesJSON], ignore_index=True)
print("Combined Shape:", df.shape)
df = df.drop_duplicates(subset="Order_ID").reset_index(drop=True)
print("Unique Orders:", len(df))
print(df.head())

# cell 5
# Calculate sales and extract date details
df["total_sales"] = df["Quantity"] * df["Price"]
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Month_name"] = df["Date"].dt.month_name()

# cell 6
print(df.head())

# cell 7
# Sales analysis
total_sales = df["total_sales"].sum()
average_order_value = df["total_sales"].mean()

print("Total Sales:", round(total_sales, 2))
print("Average Order Value:", round(average_order_value, 2))

# cell 8
# Compare product sales
product_sales = df.groupby("Product")["total_sales"].sum()
print(product_sales)
product_sales.plot(kind="bar", figsize=(8, 5))
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# cell 9
# Monthly sales trend
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["total_sales"].sum()
monthly_sales.plot(kind="bar", figsize=(8, 5))
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()