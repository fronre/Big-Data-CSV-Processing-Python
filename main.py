import pandas as pd
import dask.dataframe as dd
import time
import os
import matplotlib.pyplot as plt

FILE_PATH = "data/ACI-IoT-2023-Payload.csv"
COMPRESSED_PATH = "data/compressed.csv.gz"
RESULTS_FILE = "result/results.csv"
GRAPH_FILE = "result/comparison.png"

results = []

# =========================
# Pandas Chunks
# =========================
start = time.time()
row_count = 0
for chunk in pd.read_csv(FILE_PATH, chunksize=100000):
    row_count += len(chunk)
pandas_time = round(time.time() - start, 2)

results.append(["Pandas Chunks", pandas_time])

# =========================
# Dask
# =========================
start = time.time()
df = dd.read_csv(FILE_PATH)
rows = df.shape[0].compute()
dask_time = round(time.time() - start, 2)

results.append(["Dask", dask_time])

# =========================
# Compression
# =========================
start = time.time()
df_small = pd.read_csv(FILE_PATH)
df_small.to_csv(COMPRESSED_PATH, compression="gzip")
compression_time = round(time.time() - start, 2)

results.append(["Compression", compression_time])

# =========================
# File Sizes
# =========================
original_size = round(os.path.getsize(FILE_PATH)/(1024**2),2)
compressed_size = round(os.path.getsize(COMPRESSED_PATH)/(1024**2),2)

# =========================
# Save Results to CSV
# =========================
df_results = pd.DataFrame(results, columns=["Method", "Execution Time (sec)"])
df_results["Original Size (MB)"] = original_size
df_results["Compressed Size (MB)"] = compressed_size

df_results.to_csv(RESULTS_FILE, index=False)

print("\nResults saved to", RESULTS_FILE)

# =========================
# Save Graph
# =========================
plt.figure()
plt.bar(df_results["Method"], df_results["Execution Time (sec)"])
plt.xlabel("Method")
plt.ylabel("Execution Time (sec)")
plt.title("Performance Comparison")
plt.savefig(GRAPH_FILE)
plt.close()

print("Graph saved to", GRAPH_FILE)