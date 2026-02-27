import dask.dataframe as dd
from utils.timer import measure_performance

@measure_performance
def read_with_dask(file_path):
    
    df = dd.read_csv(
        file_path,
        blocksize="64MB",   # تقسيم أفضل
        dtype=str           # يقلل استهلاك RAM
    )

    return df.map_partitions(len).compute().sum()