from services.pandas_chunks import read_with_chunks
from services.dask_reader import read_with_dask
from services.compressor import compress_file

import os
import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = "data/ACI-IoT-2023-Payload.csv"
COMPRESSED_PATH = "data/compressed.csv.gz"
RESULTS_FILE = "result/results.csv"
GRAPH_TIME_FILE = "result/time_comparison.png"
GRAPH_MEMORY_FILE = "result/memory_comparison.png"


def main():

    results = []

    # ========================
    # Pandas
    # ========================
    rows, pandas_time, pandas_memory = read_with_chunks(FILE_PATH)
    results.append(["Pandas Chunks", pandas_time, pandas_memory])

    # ========================
    # Dask
    # ========================
    rows, dask_time, dask_memory = read_with_dask(FILE_PATH)
    results.append(["Dask", dask_time, dask_memory])

    # ========================
    # Compression
    # ========================
    _, compression_time, compression_memory = compress_file(FILE_PATH, COMPRESSED_PATH)
    results.append(["Compression", compression_time, compression_memory])

    # ========================
    # File Sizes
    # ========================
    original_size = round(os.path.getsize(FILE_PATH) / (1024**2), 2)
    compressed_size = round(os.path.getsize(COMPRESSED_PATH) / (1024**2), 2)

    # ========================
    # Save Results
    # ========================
    df_results = pd.DataFrame(
        results,
        columns=["Method", "Execution Time (sec)", "Peak Memory (MB)"]
    )

    df_results["Original Size (MB)"] = original_size
    df_results["Compressed Size (MB)"] = compressed_size

    df_results.to_csv(RESULTS_FILE, index=False)
    print("Results saved to", RESULTS_FILE)

    # ========================
    # Time Graph
    # ========================
    plt.figure()
    plt.bar(df_results["Method"], df_results["Execution Time (sec)"])
    plt.xlabel("Method")
    plt.ylabel("Execution Time (sec)")
    plt.title("Execution Time Comparison")
    plt.savefig(GRAPH_TIME_FILE)
    plt.close()

    print("Time graph saved to", GRAPH_TIME_FILE)

    # ========================
    # Memory Graph
    # ========================
    plt.figure()
    plt.bar(df_results["Method"], df_results["Peak Memory (MB)"])
    plt.xlabel("Method")
    plt.ylabel("Peak Memory (MB)")
    plt.title("Memory Usage Comparison")
    plt.savefig(GRAPH_MEMORY_FILE)
    plt.close()

    print("Memory graph saved to", GRAPH_MEMORY_FILE)


if __name__ == "__main__":
    main()