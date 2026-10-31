#Step 1

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("Iris.csv")

print(df.head())
print(df.shape)


#Step 2

# Remove unnecessary columns
X = df.drop(columns=["Id", "Species"], errors="ignore")

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Data preprocessing completed")


#Step 3

inertia = []

for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled)
    inertia.append(model.inertia_)

# Plot elbow graph
plt.plot(range(1, 11), inertia, marker="o")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

#Step 4

# Create K-Means model with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

# Fit model and assign clusters
df["Cluster"] = kmeans.fit_predict(X_scaled)

print(df[["Cluster"]].head(10))
print("\nCluster counts:")
print(df["Cluster"].value_counts().sort_index())


#Step 5

plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=df["Cluster"],
    cmap="viridis"
)

plt.xlabel("Sepal Length (standardized)")
plt.ylabel("Sepal Width (standardized)")
plt.title("K-Means Clustering on Iris Dataset")
plt.show()
