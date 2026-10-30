# Practical: Dimensionality Reduction using PCA
# !pip install pandas matplotlib scikit-learn

# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os

# Step 2: Load the dataset
file_path = "Wine.csv"
if os.path.exists(file_path):
    dataset = pd.read_csv(file_path)
else:
    url = "https://media.geeksforgeeks.org/wp-content/uploads/Wine.csv"
    dataset = pd.read_csv(url)

# Step 3: Separate features and target
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Step 4: Standardize the features
sc = StandardScaler()
X = sc.fit_transform(X)

# Step 5: Apply PCA to reduce to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Step 6: Display explained variance
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

print("Total Variance Retained:",
      round(sum(pca.explained_variance_ratio_) * 100, 2), "%")


# Step 7: Visualize PCA
plt.figure(figsize=(8,5))

plt.scatter(X_pca[y==1, 0], X_pca[y==1, 1],
            color='red', label='Class 1')

plt.scatter(X_pca[y==2, 0], X_pca[y==2, 1],
            color='blue', label='Class 2')

plt.scatter(X_pca[y==3, 0], X_pca[y==3, 1],
            color='green', label='Class 3')

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Visualization")
plt.legend()
plt.show()


#Graph 2
plt.figure(figsize=(8,5))

plt.scatter(X_pca[y==1, 0], X_pca[y==1, 1],
            color='red', label='Class 1')

plt.scatter(X_pca[y==2, 0], X_pca[y==2, 1],
            color='blue', label='Class 2')

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Visualization")

plt.legend()
plt.show()
