import pandas as pd
import gzip
from utils.timer import measure_time

@measure_time
def compress_file(input_path, output_path, chunk_size=100000):
    with gzip.open(output_path, 'wt', newline='') as f_out:
        for i, chunk in enumerate(pd.read_csv(input_path, chunksize=chunk_size)):
            chunk.to_csv(
                f_out,
                header=(i == 0),
                index=False
            )