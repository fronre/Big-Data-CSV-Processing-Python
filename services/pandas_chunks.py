import pandas as pd
from utils.timer import measure_performance

@measure_performance
def read_with_chunks(file_path, chunk_size=1000):
    row_count = 0
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        row_count += len(chunk)
    return row_count