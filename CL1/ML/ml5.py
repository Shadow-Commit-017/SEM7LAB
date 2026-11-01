#Step 1

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("car_evaluation.csv", header=None)

# Assign column names
df.columns = [
    "buying", "maint", "doors",
    "persons", "lug_boot", "safety", "class"
]

print(df.head())
print("Dataset shape:", df.shape)

#Step 2

# Separate input features and target
X = df.drop("class", axis=1)
y = df["class"]

# Convert categorical features into numerical values
X = pd.get_dummies(X)

print("Preprocessing completed")
print(X.head())

#Step 3

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

#Step 4

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

print("Random Forest model trained successfully")

#Step 5

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Accuracy percentage:", accuracy * 100, "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


#Step 6

# Example car details
new_car = pd.DataFrame([{
    "buying": "low",
    "maint": "low",
    "doors": "4",
    "persons": "4",
    "lug_boot": "big",
    "safety": "high"
}])

# Apply the same encoding as training data
new_car_encoded = pd.get_dummies(new_car)
new_car_encoded = new_car_encoded.reindex(
    columns=X.columns,
    fill_value=0
)

# Predict car acceptability
prediction = model.predict(new_car_encoded)

print("Predicted car category:", prediction[0])
