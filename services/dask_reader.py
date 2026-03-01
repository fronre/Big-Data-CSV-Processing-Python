import dask.dataframe as dd
import psutil
import os
from utils.timer import measure_performance

@measure_performance
def read_with_dask(file_path):

    process = psutil.Process(os.getpid())
    peak_memory = 0

    df = dd.read_csv(
        file_path,
        blocksize="64MB",   # تقسيم أفضل
        dtype=str           # يقلل استهلاك RAM
    )

    # تنفيذ الحساب
    total_rows = df.map_partitions(len).compute().sum()

    # نحسب الميموار بعد الـ compute (أعلى نقطة عادة تكون هنا)
    current_memory = process.memory_info().rss / (1024 ** 2)
    peak_memory = max(peak_memory, current_memory)

    return total_rows, round(peak_memory, 2)