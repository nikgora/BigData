from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Генерація даних
X, _ = make_blobs(n_samples=900, centers=4, random_state=42)

# Виконання спектральної кластеризації
clustering = SpectralClustering(n_clusters=4, assign_labels='kmeans', random_state=42).fit(X)

# Візуалізація результатів
plt.scatter(X[:, 0], X[:, 1], c=clustering.labels_, cmap='viridis')
plt.show()
