import numpy as np
from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

# Завантажуємо дані
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Масштабуємо ознаки
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Розділяємо дані
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Визначаємо параметри для GridSearchCV
param_grid = {
    'C': [0.1, 1, 10, 100, 1000, 100000],
    'gamma': [1, 0.1, 0.01, 0.001, 0.0001, 0.00001],
    'kernel': ['rbf', 'poly', 'sigmoid', 'linear'],
    'degree': [2, 3, 4, 5, 6, 7, 8, 9, 10],
}

# Створюємо модель SVM
svc = svm.SVC()

# Налаштовуємо параметри за допомогою GridSearchCV
grid = GridSearchCV(svc, param_grid, refit=True, verbose=2, cv=10)
grid.fit(X_train, y_train)

# Виводимо найкращі параметри
print("Найкращі параметри:")
print(grid.best_params_)

# Прогнозуємо та оцінюємо модель
grid_predictions = grid.predict(X_test)
print(classification_report(y_test, grid_predictions))
