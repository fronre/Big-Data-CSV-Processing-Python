import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        print(f"\nRunning {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution Time:", round(end - start, 2), "seconds")
        return result
    return wrapper