from collections import defaultdict


def map_reduce_matrix_multiplication(A, B):
    # Перевіряємо, чи можна множити матриці
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must be equal to number of rows in B")

    # Map phase
    mapped_values = []

    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                mapped_values.append(((i, k), A[i][j] * B[j][k]))

    # Reduce phase
    reduced_values = defaultdict(int)
    for key, value in mapped_values:
        reduced_values[key] += value

    # Формуємо результуючу матрицю
    n_rows = len(A)
    n_cols = len(B[0])
    result = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

    for (i, k), value in reduced_values.items():
        result[i][k] = value

    return result


def map_reduce_example():
    # Приклад використання
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    C = map_reduce_matrix_multiplication(A, B)

    print("Resultant Matrix C:")
    for row in C:
        print(row)


if __name__ == "__main__":
    map_reduce_example()
