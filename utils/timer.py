import time
import psutil
import os

def measure_performance(func):
    def wrapper(*args, **kwargs):

        process = psutil.Process(os.getpid())
        start_memory = process.memory_info().rss / (1024 ** 2)

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        end_memory = process.memory_info().rss / (1024 ** 2)

        execution_time = round(end_time - start_time, 2)
        peak_memory = round(end_memory - start_memory, 2)

        return result, execution_time, peak_memory

    return wrapper