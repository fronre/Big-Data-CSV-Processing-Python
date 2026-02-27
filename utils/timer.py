import time
from functools import wraps
from memory_profiler import memory_usage

def measure_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.time()

        mem_usage = memory_usage(
            (func, args, kwargs),
            interval=0.1,
            retval=True
        )

        memory_list, result = mem_usage

        execution_time = round(time.time() - start_time, 2)
        peak_memory = round(max(memory_list), 2)

        return result, execution_time, peak_memory

    return wrapper