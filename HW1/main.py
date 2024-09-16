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


# Функція для багатопотокового розбиття масиву на чанки
def split_array_parallel(arr, num_chunks, thread_pool):
    chunk_size = len(arr) // num_chunks

    # Функція для вилучення одного чанка
    def get_chunk(i):
        return arr[i * chunk_size:(i + 1) * chunk_size]

    # Паралельне розбиття масиву
    chunk_indices = list(range(num_chunks))
    with thread_pool as executor:
        chunks = list(executor.map(get_chunk, chunk_indices))

    # Додаємо елементи, що залишилися, в останній чанк, якщо є
    remaining_elements = len(arr) % num_chunks
    if remaining_elements > 0:
        chunks[-1].extend(arr[-remaining_elements:])

    return chunks

# Реалізація через MapReduce
def find_max_mapreduce(arr, num_threads, thread_pool):
    start_time = time.time()

    # Параллельное разбиение на чанки
    chunks = split_array_parallel(arr, num_threads, thread_pool)

    end_time = time.time()
    print(f"Time for splitting into chunks: {end_time - start_time} seconds")
    split_time = end_time - start_time
    # Параллельне обчислення максимумів для кожної частини
    start_time = time.time()
    with ThreadPoolExecutor(num_threads) as executor:
        end_time = time.time()
        print(f"Time for thread creation: {end_time - start_time} seconds")
        max_values = list(executor.map(find_max_chunk, chunks))

    # Знаходимо загальний максимум
    return max(max_values), split_time


# Генерація випадкового масиву
def generate_random_array(size):
    return [random.randint(-1923919391293, 8412931133123) for _ in range(size)]


# Введення кількості елементів від користувача
size = int(input("Введіть кількість елементів у масиві: "))
num_threads = int(input("Введіть кількість потоків для MapReduce: "))
thread_pool = ThreadPoolExecutor(num_threads)

# Генеруємо випадковий масив
arr = generate_random_array(size)

# Вбудована реалізація
start_time = time.time()
max_value_standard = max(arr)
end_time = time.time()
print(f"Max value (max(arr)): {max_value_standard}, Time: {end_time - start_time} seconds")

# Стандартна реалізація
start_time = time.time()
max_value_standard = find_max_standard(arr)
end_time = time.time()
print(f"Max value (standard): {max_value_standard}, Time: {end_time - start_time} seconds")

# MapReduce реалізація
start_time = time.time()
max_value_mapreduce, split_time = find_max_mapreduce(arr, num_threads, thread_pool)
end_time = time.time()
print(f"Max value (MapReduce): {max_value_mapreduce}, Time: {end_time - start_time} seconds, Time with out splitting in chunks: {end_time - start_time - split_time} seconds")
# Введіть кількість елементів у масиві: 100000
# Введіть кількість потоків для MapReduce: 100
# Max value (max(arr)): 8412893583015, Time: 0.0009996891021728516 seconds
# Max value (standard): 8412893583015, Time: 0.0019989013671875 seconds
# Time for splitting into chunks: 0.011616706848144531 seconds
# Time for thread creation: 0.0 seconds
# Max value (MapReduce): 8412893583015, Time: 0.018630504608154297 seconds, Time with out splitting in chunks: 0.007013797760009766 seconds
#
# Process finished with exit code 0


