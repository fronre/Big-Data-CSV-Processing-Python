import pandas as pd
import psutil
import os
from utils.timer import measure_performance

@measure_performance
def read_with_chunks(file_path, chunk_size=1000):
    process = psutil.Process(os.getpid())
    peak_memory = 0
    row_count = 0

    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        row_count += len(chunk)

        # نحسب الميموار في كل دورة
        current_memory = process.memory_info().rss / (1024 ** 2)
        peak_memory = max(peak_memory, current_memory)

    # نرجع عدد الصفوف و الـ peak memory
    return row_count, round(peak_memory, 2)