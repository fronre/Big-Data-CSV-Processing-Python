import dask.dataframe as dd
from utils.timer import measure_time

@measure_time
def read_with_dask(file_path):
    df = dd.read_csv(file_path)
    return df.shape[0].compute()