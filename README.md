# 🚀 High-Performance CSV Processing (5GB+)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Dask](https://img.shields.io/badge/Dask-Parallel%20Computing-green)
![Status](https://img.shields.io/badge/Project-Academic-blueviolet)

---

## 📌 Project Overview

This project demonstrates efficient techniques for processing very large CSV files (~5GB) in Python without causing memory overflow.

The experiment compares different Big Data approaches in terms of:

- ⏱ Execution time  
- 💾 Storage efficiency  
- 🧠 Memory management  

### Dataset Used

- File name: `ACI-IoT-2023-Payload.csv`
- File size: **5276.13 MB (~5.2 GB)**

> ⚠ Dataset not included in this repository due to its large size.

---

## 🏗 Project Structure

```
High-Performance-CSV-Processing/
│
├── services/
│   ├── pandas_chunks.py
│   ├── dask_reader.py
│   └── compressor.py
│
├── utils/
│   └── timer.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Technologies Used

- Python 3.x  
- Pandas  
- Dask  
- Matplotlib  
- gzip  

---

## 🔬 Methods Implemented

### 1️⃣ Pandas Chunking

```python
pd.read_csv(file, chunksize=100000)
```

✔ Memory efficient  
✔ Stable  
❌ Sequential processing  

**Execution Time:** `40.63 seconds`

---

### 2️⃣ Dask (Parallel Processing)

```python
dd.read_csv(file)
```

✔ Fastest method  
✔ Multi-core processing  
✔ Designed for large datasets  

**Execution Time:** `25.31 seconds`

---

### 3️⃣ File Compression (gzip)

- Original Size: **5276.13 MB**
- Compressed Size: **2968.57 MB**
- Storage Reduction: **~44%**

✔ Reduces disk usage  
❌ High processing time  

**Execution Time:** `295.48 seconds`

---

## 📊 Experimental Results

| Method          | Execution Time (sec) | File Size (MB) |
|----------------|----------------------|----------------|
| Pandas Chunks | 40.63               | 5276.13       |
| Dask          | 25.31               | 5276.13       |
| Compression   | 295.48              | 2968.57       |

---

## 📈 Performance Analysis

- 🥇 **Fastest Approach:** Dask  
- 💾 **Best Storage Optimization:** Compression (~44% reduction)  
- ⚖ **Balanced Approach:** Pandas Chunking  

Dask outperformed Pandas due to parallel computation.  
Compression significantly reduced storage size but required much more processing time.

---

## 🧠 Key Takeaways

- Large CSV files cannot be safely loaded entirely into memory.
- Chunking improves memory control.
- Parallel processing significantly improves execution speed.
- Compression trades CPU time for storage efficiency.

---

## ▶️ How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

## 🎯 Conclusion

This project demonstrates practical and scalable techniques for handling large-scale datasets efficiently in Python.

- Use **Dask** for performance-critical workloads.
- Use **Compression** for storage optimization.
- Use **Pandas chunking** for controlled memory usage.
