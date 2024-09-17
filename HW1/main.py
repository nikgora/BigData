import random
import time
from multiprocessing import Pool, cpu_count


# Function for finding the maximum in a part of an array
def find_max_chunk(chunk):
    return max(chunk)


# Standard method for finding the maximum
def find_max_standard(arr):
    if len(arr) == 0:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


# Function for splitting an array into chunks
def split_array(arr, num_chunks):
    chunk_size = len(arr) // num_chunks
    chunks = [arr[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks)]

    # Add the remaining elements to the last chunk, if any
    remaining_elements = len(arr) % num_chunks
    if remaining_elements > 0:
        chunks[-1].extend(arr[-remaining_elements:])

    return chunks


# Implementation via MapReduce using multiprocessing
def find_max_mapreduce(arr, num_processes):
    start_time = time.time()

    # Split the array into chunks
    chunks = split_array(arr, num_processes)

    end_time = time.time()
    print(f"Time for splitting into chunks: {end_time - start_time} seconds")
    split_time = end_time - start_time

    # Parallel calculation of max for each chunk using multiprocessing
    start_time = time.time()
    with Pool(processes=num_processes) as pool:
        max_values = pool.map(find_max_chunk, chunks)

    end_time = time.time()
    print(f"Time for processing chunks: {end_time - start_time} seconds")

    # Find the total maximum
    return max(max_values), split_time


# Generate a random array
def generate_random_array(size):
    return [random.randint(-1923919391293, 8412931133123) for _ in range(size)]

if __name__ == '__main__':
    # Input the number of elements from the user
    size = int(input("Enter the number of elements in the array: "))
    num_processes = int(input(f"Enter the number of processes for MapReduce (maximum {cpu_count()}): "))

    # Generate random array
    arr = generate_random_array(size)

    # Built-in implementation
    start_time = time.time()
    max_value_builtin = max(arr)
    end_time = time.time()
    print(f"Max value (max(arr)): {max_value_builtin}, Time: {end_time - start_time} seconds")

    # Standard implementation
    start_time = time.time()
    max_value_standard = find_max_standard(arr)
    end_time = time.time()
    print(f"Max value (standard): {max_value_standard}, Time: {end_time - start_time} seconds")

    # MapReduce implementation with multiprocessing
    start_time = time.time()
    max_value_mapreduce, split_time = find_max_mapreduce(arr, num_processes)
    end_time = time.time()
    print(
        f"Max value (MapReduce): {max_value_mapreduce}, Time: {end_time - start_time} seconds, Time without splitting: {end_time - start_time - split_time} seconds")
