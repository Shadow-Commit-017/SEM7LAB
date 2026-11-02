
# Agglomerative Hierarchical Clustering

# Step 1: Import required libraries
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

# Step 2: Load Iris dataset
iris = load_iris()
X = iris.data

print("Dataset loaded successfully")
print("Total number of records:", len(X))

# Step 3: Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Apply Agglomerative Clustering
model = AgglomerativeClustering(
    n_clusters=3,
    linkage='ward'
)

labels = model.fit_predict(X_scaled)

# Step 5: Display cluster labels
print("\nCluster Labels:")
print(labels)

# Step 6: Display number of clusters
print("\nNumber of clusters:", len(set(labels)))

# Step 7: Visualize clusters
plt.figure(figsize=(8, 5))

plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=labels,
    cmap='rainbow'
)

plt.title("Agglomerative Hierarchical Clustering")
plt.xlabel("Sepal Length (Standardized)")
plt.ylabel("Sepal Width (Standardized)")

plt.show()
