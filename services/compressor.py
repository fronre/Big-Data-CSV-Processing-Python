import pandas as pd

def compress_file(input_path, output_path, chunk_size=100000):
    with open(output_path, 'wb') as f_out:
        for chunk in pd.read_csv(input_path, chunksize=chunk_size):
            chunk.to_csv(f_out, header=f_out.tell()==0, index=False)