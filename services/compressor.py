import pandas as pd
import gzip
import psutil
import os
from utils.timer import measure_performance


@measure_performance
def compress_file(input_path, output_path):

    process = psutil.Process(os.getpid())
    peak_memory = 0

    # قراءة الملف كامل
    df = pd.read_csv(input_path)

    # حساب الميموري بعد القراءة
    current_memory = process.memory_info().rss / (1024 ** 2)
    peak_memory = max(peak_memory, current_memory)

    # كتابة الملف مضغوط
    with gzip.open(output_path, 'wt', newline='') as f_out:
        df.to_csv(
            f_out,
            index=False
        )

    return output_path, round(peak_memory, 2)