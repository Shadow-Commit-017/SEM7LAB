import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = pd.DataFrame({
    "patient_id": range(1, 21),
    "age": [45, 50, 60, 35, 55, 65, 40, 70, 48, 52,
            44, 62, 38, 58, 67, 42, 53, 63, 47, 56],
    "gene1": [10, 20, 30, 15, 25, 35, 12, 40, 18, 22,
              11, 32, 14, 28, 38, 16, 24, 34, 19, 27],
    "gene2": [5, 8, 12, 6, 10, 15, 4, 18, 7, 9,
              5, 13, 6, 11, 16, 7, 9, 14, 8, 10],
    "overall_survival_months": [60, 30, 15, 72, 24, 10, 65, 8, 48, 36,
                                70, 12, 66, 20, 9, 58, 32, 14, 50, 22],
    "overall_survival": [ 0, 1, 1, 0, 1, 1, 0, 1, 0, 0,
                          0, 1, 0, 1, 1, 0, 0, 1, 0, 1]
})

X = data[["age", "gene1", "gene2"]]
y = data["overall_survival"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

X_train = X_train.fillna(X_train.median())
X_test = X_test.fillna(X_train.median())

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

prediction = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, prediction))
print("Confusion Matrix:\n", confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction, zero_division=0))

print("Feature Importance:")
print(pd.Series(model.feature_importances_, index=X.columns)
      .sort_values(ascending=False).head(10))
