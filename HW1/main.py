import random
import time
from concurrent.futures import ThreadPoolExecutor


# Функція для знаходження максимума в частині масиву
def find_max_chunk(chunk):
    return max(chunk)


# Стандартний метод для пошуку максимума
def find_max_standard(arr):
    if len(arr) == 0:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


# Реалізація через MapReduce
def find_max_mapreduce(arr, num_threads, thread_pool):
    start_time = time.time()
    chunk_size = len(arr) // num_threads
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
    end_time = time.time()
    print(f"Time for cropped in chunks: {end_time - start_time} seconds")

    # Паралельне обчислення максимумів для кожної частини
    start_time = time.time()
    with thread_pool as executor:
        end_time = time.time()
        print(f"Time for create thread: {end_time - start_time} seconds")
        max_values = list(executor.map(find_max_chunk, chunks))

    # Знаходимо загальний максимум
    return max(max_values)


# Генерація випадкового масиву
def generate_random_array(size):
    return [random.randint(-1000, 1000) for _ in range(size)]


# Введення кількості елементів від користувача
size = int(input("Введіть кількість елементів у масиві: "))
num_threads = int(input("Введіть кількість потоків для MapReduce: "))
thread_pool = ThreadPoolExecutor(num_threads)
# Генеруємо випадковий масив
arr = generate_random_array(size)

# Стандартна реалізація
start_time = time.time()
max_value_standard = find_max_standard(arr)
end_time = time.time()
print(f"Max value (standard): {max_value_standard}, Time: {end_time - start_time} seconds")

# MapReduce реалізація
start_time = time.time()
max_value_mapreduce = find_max_mapreduce(arr, num_threads, thread_pool)
end_time = time.time()
print(f"Max value (MapReduce): {max_value_mapreduce}, Time: {end_time - start_time} seconds")
# :\BigData\HW1\.venv\Scripts\python.exe E:\BigData\HW1\main.py
# Введіть кількість елементів у масиві: 1000000000
# Введіть кількість потоків для MapReduce: 100
# Max value (standard): 1000, Time: 2283.100380420685 seconds
# Max value (MapReduce): 1000, Time: 18808.188708782196 seconds

# Введіть кількість елементів у масиві: 10000000
# Введіть кількість потоків для MapReduce: 1000
# Max value (standard): 1000, Time: 0.16844725608825684 seconds
# Time for cropped in chunks: 0.11290359497070312 seconds
# Max value (MapReduce): 1000, Time: 0.4196147918701172 seconds
#
# Process finished with exit code 0

