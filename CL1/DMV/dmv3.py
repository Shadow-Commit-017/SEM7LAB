# cell 1
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("Telecom_Customer_Churn.csv")
print(data.head())
data.info()
print("Shape:", data.shape)

# cell 2
# Standardize text and convert data types
for col in data.select_dtypes(include="object").columns:
    data[col] = data[col].str.strip().replace("", np.nan)
data["gender"] = data["gender"].str.lower()
data["TotalCharges"] = pd.to_numeric(data["TotalCharges"], errors="coerce")
print("Missing Values:")
print(data.isnull().sum())

data = data.drop_duplicates().copy()
print("After removing duplicates:", data.shape)

# cell 3
# Split before fitting preprocessing values
train, test = train_test_split(data, test_size=0.2, random_state=42, stratify=data["Churn"])
train = train.copy()
test = test.copy()
print("Training Shape:", train.shape)
print("Testing Shape:", test.shape)

# cell 4
# Fill missing values using training data
num_cols = train.select_dtypes(include=np.number).columns
medians = train[num_cols].median()
train[num_cols] = train[num_cols].fillna(medians)
test[num_cols] = test[num_cols].fillna(medians)

cat_cols = train.select_dtypes(include="object").columns.drop(["customerID", "Churn"])
for col in cat_cols:
    mode = train[col].mode()[0]
    train[col] = train[col].fillna(mode)
    test[col] = test[col].fillna(mode)

for frame in [train, test]:
    frame["SeniorCitizen"] = frame["SeniorCitizen"].astype(int)
print("Training missing values:", train.isnull().sum().sum())
print("Testing missing values:", test.isnull().sum().sum())

# cell 5
# Create new features and handle zero tenure separately
for frame in [train, test]:
    frame["AvgMonthlyCharge"] = frame["TotalCharges"] / frame["tenure"].replace(0, np.nan)
    frame["AvgMonthlyCharge"] = frame["AvgMonthlyCharge"].fillna(frame["MonthlyCharges"])
    frame["TenureGroup"] = pd.cut(
        frame["tenure"], bins=[0, 12, 24, 48, 100],
        labels=["New", "Medium", "Long", "Very Long"], include_lowest=True
    )

# cell 6
# Handle outliers using training IQR bounds
scale_cols = ["tenure", "MonthlyCharges", "TotalCharges", "AvgMonthlyCharge"]
for col in scale_cols:
    Q1 = train[col].quantile(0.25)
    Q3 = train[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    print(col, "training outliers:", ((train[col] < lower) | (train[col] > upper)).sum())
    train[col] = train[col].clip(lower, upper)
    test[col] = test[col].clip(lower, upper)

# cell 7
# Export cleaned records before encoding and scaling
cleaned = pd.concat([train, test]).sort_index()
cleaned.to_csv("Telecom_Customer_Churn_Cleaned.csv", index=False)
print(cleaned.head())
print("Cleaned Shape:", cleaned.shape)
print("Saved Telecom_Customer_Churn_Cleaned.csv")

# cell 8
# Separate features and target, then encode categories
X_train = pd.get_dummies(train.drop(columns=["customerID", "Churn"]), drop_first=True, dtype=int)
X_test = pd.get_dummies(test.drop(columns=["customerID", "Churn"]), dtype=int)
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)
y_train = train["Churn"].map({"No": 0, "Yes": 1})
y_test = test["Churn"].map({"No": 0, "Yes": 1})

# cell 9
# Scale continuous features using training data
scaler = StandardScaler()
X_train[scale_cols] = scaler.fit_transform(X_train[scale_cols])
X_test[scale_cols] = scaler.transform(X_test[scale_cols])
print("Training Features:")
print(X_train.head())
print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)