import sys
import os
import pandas as pd
from csv import DictReader

if len(sys.argv) < 3:
    print("[!] Invalid number of arguments")
    print("[!] Usage: python csv-combiner.py [filepath1.csv, filepath2.csv, etc] > [outputfile.csv]")
    exit(1)

inputs = sys.argv
output_file = inputs[-1]
input_files = inputs[1: len(inputs)-1]
new_data = []
for file in input_files:
    filename = os.path.basename(file)
    with open(file, 'r') as f:
        dict_reader = DictReader(f)
    f.close()
    for d in list(dict_reader):
        d["filename"] = filename
    new_data.append(list(dict_reader))
new_data_df = pd.DataFrame(new_data)
print(new_data_df)
new_data_df.to_csv(output_file, index=False)






