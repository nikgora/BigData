import time
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_moons

# Приклад, де алгоритм працює добре (опуклі кластери)
# Генеруємо дані
from sklearn.datasets import make_blobs
X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0)

# Застосовуємо k-середніх
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Візуалізація результатів
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.75)
plt.title("Опуклі кластери")
plt.show()

# Приклад, де алгоритм працює погано (неопуклі кластери)
# Генеруємо дані
X, y = make_moons(n_samples=300, noise=0.05, random_state=0)

# Застосовуємо k-середніх
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Візуалізація результатів
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.title("Неопуклі кластери")
plt.show()

# Вплив параметрів алгоритму на результат та час виконання
# Генеруємо дані
X, y_true = make_blobs(n_samples=1000, centers=5,
                       cluster_std=0.60, random_state=0)

params = [
    {'n_clusters': 5, 'init': 'k-means++', 'max_iter': 300, 'n_init': 10},
    {'n_clusters': 5, 'init': 'random', 'max_iter': 300, 'n_init': 10},
    {'n_clusters': 5, 'init': 'k-means++', 'max_iter': 100, 'n_init': 10},
    {'n_clusters': 5, 'init': 'k-means++', 'max_iter': 300, 'n_init': 1},
]

times = []
inertias = []

for param in params:
    start_time = time.time()
    kmeans = KMeans(**param)
    kmeans.fit(X)
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)
    inertias.append(kmeans.inertia_)

# Виведемо результати
for i, param in enumerate(params):
    print(f"Параметри: {param}")
    print(f"Час виконання: {times[i]:.4f} секунд")
    print(f"Inertia: {inertias[i]:.2f}")
    print("-" * 30)

# Зміна дистанції всередині кластерів з кожним кроком
# Генеруємо дані
X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0)

# Ініціалізуємо k-середніх
kmeans = KMeans(n_clusters=4, init='random', n_init=1, max_iter=1, verbose=0)
inertias = []

for i in range(1, 11):
    kmeans.max_iter = i
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

# Візуалізація зміни інерції
plt.plot(range(1, 11), inertias, marker='o')
plt.title('Зміна інерції з кожною ітерацією')
plt.xlabel('Номер ітерації')
plt.ylabel('Inertia')
plt.show()
