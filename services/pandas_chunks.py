import pandas as pd
from utils.timer import measure_time

@measure_time
def read_with_chunks(file_path, chunk_size=100000):
    row_count = 0
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        row_count += len(chunk)
    return row_count