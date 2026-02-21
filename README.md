# Big Data CSV Performance Comparison

## Project Overview
This project compares different techniques for handling large CSV files (5GB+) in Python.

## Methods Used
- Pandas with chunks
- Dask (parallel processing)
- File compression (gzip)

## Results

Original Size: 5276.13 MB  
Compressed Size: 2968.57 MB  

Execution Time:
- Pandas Chunks: 40.63 seconds
- Dask: 25.31 seconds
- Compression: 295.48 seconds

## Conclusion
Dask was the fastest method due to parallel processing.  
Pandas chunks reduced memory usage but was slower.  
Compression reduced file size (~44%) but required the longest execution time.

## How to Run
```bash
pip install -r requirements.txt
python main.py
