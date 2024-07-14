import time
import os
import concurrent.futures

def create_file_with_delay(filename):
    time.sleep(1)
    with open(filename, 'w') as f:
        f.write("This is a test file.")

def sequential_execution():
    start_time = time.time()

    for i in range(100):
        create_file_with_delay(f"file_{i}.txt")

    end_time = time.time()
    print(f"Time taken for sequential execution: {end_time - start_time} seconds")

def multithreaded_execution():
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(create_file_with_delay, f"file_{i}.txt") for i in range(100)]
        concurrent.futures.wait(futures)

    end_time = time.time()
    print(f"Time taken for multithreaded execution: {end_time - start_time} seconds")

print("Sequential Execution:")
sequential_execution()

print("Multithreaded Execution:")
multithreaded_execution()
