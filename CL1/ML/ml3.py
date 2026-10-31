#STEP 1

import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load handwritten digits dataset
digits = load_digits()

X = digits.data
y = digits.target

print("Dataset loaded successfully")
print("Total images:", len(X))
print("Number of classes:", len(set(y)))


#STEP 2

# Display first 10 digit images
fig, axes = plt.subplots(2, 5, figsize=(10, 5))

for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap="gray")
    ax.set_title(f"Label: {digits.target[i]}")
    ax.axis("off")

plt.show()


#STEP 3

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


#STEP 4

# Create SVM classifier
model = SVC(kernel="linear")

# Train the model
model.fit(X_train, y_train)

print("SVM model trained successfully")


#STEP 5

# Predict test images
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Accuracy percentage:", accuracy * 100, "%")

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


#STEP 6

# Predict one test image
index = 0

plt.imshow(X_test[index].reshape(8, 8), cmap="gray")
plt.title("Actual Digit: " + str(y_test[index]))
plt.axis("off")
plt.show()

prediction = model.predict([X_test[index]])

print("Predicted Digit:", prediction[0])



