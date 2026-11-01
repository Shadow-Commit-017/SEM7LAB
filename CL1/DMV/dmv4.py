# cell 1
import pandas as pd
import numpy as np

df = pd.read_csv("RealEstate_Prices.csv")
print(df.head())
df.info()
print("\nMissing Values:")
print(df.isnull().sum())

# cell 2
# Clean column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^a-zA-Z0-9_]", "", regex=True)
)

# cell 3
# Remove duplicates, extra spaces and missing values
df = df.drop_duplicates().copy()

for col in df.select_dtypes("object"):
    df[col] = df[col].str.strip()

df = df.dropna()

# cell 4
# Identify and cap outliers in continuous measurements
for col in ["price", "area"]:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    print(col, "outliers:", ((df[col] < lower) | (df[col] > upper)).sum())
    df[col] = df[col].clip(lower, upper)

# cell 5
# Select large furnished properties
large_furnished = df.loc[(df["area"] >= 5000) & (df["furnishingstatus"] == "furnished")].copy()
print("Large Furnished Properties:")
print(large_furnished.head())
print("Subset Shape:", large_furnished.shape)

# cell 6
# Average prices by furnishing status
summary = df.groupby("furnishingstatus")["price"].agg(["count", "mean", "median"])
print(summary.round(2))

# cell 7
# Encode categorical variables
categorical = df.select_dtypes("object").columns
df = pd.get_dummies(df, columns=categorical, drop_first=True)
print("Cleaned Data:")
print(df.head())
print("Cleaned Shape:", df.shape)

# cell 8
# Save the cleaned dataset
df.to_csv("cleaned_realestate_prices.csv", index=False)
print("Saved cleaned_realestate_prices.csv")