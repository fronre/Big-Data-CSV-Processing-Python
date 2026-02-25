from services.pandas_chunks import read_with_chunks
from services.dask_reader import read_with_dask
from services.compressor import compress_file

import os
import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = "data/ACI-IoT-2023-Payload.csv"
COMPRESSED_PATH = "data/compressed.csv.gz"
RESULTS_FILE = "result/results.csv"
GRAPH_FILE = "result/comparison.png"


def main():

    results = []

    # Pandas
    rows, pandas_time = read_with_chunks(FILE_PATH)
    results.append(["Pandas Chunks", pandas_time])

    # Dask
    rows, dask_time = read_with_dask(FILE_PATH)
    results.append(["Dask", dask_time])

    # Compression
    _, compression_time = compress_file(FILE_PATH, COMPRESSED_PATH)
    results.append(["Compression", compression_time])

    # File Sizes
    original_size = round(os.path.getsize(FILE_PATH) / (1024**2), 2)
    compressed_size = round(os.path.getsize(COMPRESSED_PATH) / (1024**2), 2)

    # Save Results
    df_results = pd.DataFrame(results, columns=["Method", "Execution Time (sec)"])
    df_results["Original Size (MB)"] = original_size
    df_results["Compressed Size (MB)"] = compressed_size

    df_results.to_csv(RESULTS_FILE, index=False)
    print("Results saved to", RESULTS_FILE)

    # Graph
    plt.figure()
    plt.bar(df_results["Method"], df_results["Execution Time (sec)"])
    plt.xlabel("Method")
    plt.ylabel("Execution Time (sec)")
    plt.title("Performance Comparison")
    plt.savefig(GRAPH_FILE)
    plt.close()

    print("Graph saved to", GRAPH_FILE)


if __name__ == "__main__":
    main()