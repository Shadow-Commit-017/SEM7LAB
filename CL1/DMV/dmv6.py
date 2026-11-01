# cell 1
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Retail_Sales_Data.csv")
df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

print(df.head())
df.info()
print("Missing Values:")
print(df.isnull().sum())

# cell 2
# Total sales by region
regional_sales = df.groupby("Region")["SalesAmount"].sum()
regional_sales = regional_sales.sort_values(ascending=False)
print("Regional Sales:")
print(regional_sales)
print("\nTotal Sales:", round(regional_sales.sum(), 2))
print("Top Region:", regional_sales.idxmax())

# cell 3
# Compare regional sales
regional_sales.plot(kind="bar", figsize=(8, 5))
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# cell 4
# Regional sales share
regional_sales.plot(kind="pie", autopct="%1.1f%%", figsize=(6, 6))
plt.title("Regional Sales Share")
plt.ylabel("")
plt.tight_layout()
plt.show()

# cell 5
# Sales by region and product category
category_sales = df.groupby(["Region", "ProductCategory"])["SalesAmount"].sum()
category_sales = category_sales.unstack(fill_value=0)
print(category_sales)

# cell 6
# Stacked sales chart
category_sales.plot(kind="bar", stacked=True, figsize=(10, 5))
plt.title("Sales by Region and Category")
plt.xlabel("Region")
plt.ylabel("Sales Amount")
plt.xticks(rotation=0)
plt.legend(title="Category")
plt.tight_layout()
plt.show()

# cell 7
# Grouped sales chart
category_sales.plot(kind="bar", figsize=(10, 5))
plt.title("Product Category Comparison")
plt.xlabel("Region")
plt.ylabel("Sales Amount")
plt.xticks(rotation=0)
plt.legend(title="Category")
plt.tight_layout()
plt.show()