import pandas as pd
import gzip
import psutil
import os
from utils.timer import measure_performance

@measure_performance
def compress_file(input_path, output_path, chunk_size=100000):

    process = psutil.Process(os.getpid())
    peak_memory = 0

    with gzip.open(output_path, 'wt', newline='') as f_out:
        for i, chunk in enumerate(pd.read_csv(input_path, chunksize=chunk_size)):

            chunk.to_csv(
                f_out,
                header=(i == 0),
                index=False
            )

            # نحسب الميموار في كل دورة
            current_memory = process.memory_info().rss / (1024 ** 2)
            peak_memory = max(peak_memory, current_memory)

    return output_path, round(peak_memory, 2)