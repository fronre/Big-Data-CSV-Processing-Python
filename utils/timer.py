import time

def measure_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result, peak_memory = func(*args, **kwargs)
        end_time = time.time()

        execution_time = round(end_time - start_time, 2)

        return result, execution_time, peak_memory

    return wrapper