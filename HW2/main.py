import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import time

mnist = fetch_openml('mnist_784', version=1)
X = mnist.data.values
y = mnist.target.astype(int).values

# Data normalization
X_scaled = StandardScaler().fit_transform(X)

# 2. My PCA
start_time = time.time()
covariance_matrix = np.cov(X_scaled, rowvar=False)

eigen_values, eigen_vectors = np.linalg.eigh(covariance_matrix)

sorted_index = np.argsort(eigen_values)[::-1]
sorted_eigenvalues = eigen_values[sorted_index]
sorted_eigenvectors = eigen_vectors[:, sorted_index]

total_variance = np.sum(sorted_eigenvalues)
explained_variance_ratio = sorted_eigenvalues / total_variance
cumulative_variance_ratio = np.cumsum(explained_variance_ratio)

k = np.argmax(cumulative_variance_ratio >= 0.995) + 1
print(f'Selected k = {k}, which explains {cumulative_variance_ratio[k-1]*100:.2f}% of the variance.')

projection_matrix = sorted_eigenvectors[:, :k]
X_reduced_my = np.dot(X_scaled, projection_matrix)
my_time = time.time() - start_time


# Scree Plot
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, 'o-', label='Individual explained variance')
plt.plot(range(1, len(cumulative_variance_ratio) + 1), cumulative_variance_ratio, 's-', label='Cumulative explained variance')
plt.xlabel('Number of components')
plt.ylabel('Explained variance')
plt.title('Scree Plot for MNIST')
plt.legend()
plt.grid(True)
plt.show()


X_vis = X_reduced_my
y_vis = y

plt.figure(figsize=(12, 8))
scatter = plt.scatter(X_vis[:, 0], X_vis[:, 1], c=y_vis, cmap='tab10', alpha=0.7)
plt.xlabel('Principal component 1')
plt.ylabel('Principal component 2')
plt.title('PCA on MNIST dataset (first 2 components)')
plt.colorbar(scatter, label='Digit')
plt.grid(True)
plt.show()

# 3. Compare to scikit-learn PCA
pca = PCA(n_components=k)
start_time = time.time()
X_reduced_sklearn = pca.fit_transform(X_scaled)
sklearn_time = time.time() - start_time

print(f'My PCA algorithm running time: {my_time:.4f} seconds')
print(f'PCA running time with scikit-learn: {sklearn_time:.4f} seconds')

methods = ['My PCA', 'scikit-learn PCA']
times = [my_time, sklearn_time]

plt.figure(figsize=(8, 6))
plt.bar(methods, times, color=['blue', 'green'])
plt.ylabel('Time (seconds)')
plt.title('Comparison of PCA algorithms on MNIST')
plt.grid(True)
plt.show()

difference = np.abs(X_reduced_my - X_reduced_sklearn)
max_difference = np.max(difference)
print(f'Maximum difference between my PCA and scikit-learn PCA: {max_difference:.6e}')
