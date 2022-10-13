import sys
import os
import pandas as pd

if len(sys.argv) < 3:
    print("[!] Invalid number of arguments")
    print("[!] Usage: python csv-combiner.py [filepath1.csv filepath2.csv etc] [outputfile.csv]")
    exit(1)

inputs = sys.argv
input_files = inputs[1: len(inputs)-1]
output_file = inputs[-1]
combined_data_df = pd.DataFrame()
for file in input_files:
    filename = os.path.basename(file)
    print(file)
    current_data_df = pd.read_csv(file)
    current_data_df["filename"] = filename
    if combined_data_df.empty:
        combined_data_df = current_data_df
    else:
        combined_data_df = pd.concat([combined_data_df, current_data_df], ignore_index=True)
combined_data_df.to_csv(output_file, index=False)
print(combined_data_df)







