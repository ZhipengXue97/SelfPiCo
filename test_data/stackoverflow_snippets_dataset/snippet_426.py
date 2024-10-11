# Extracted from https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe
import pandas as pd
import os

new_df = pd.DataFrame()
for r, d, f in os.walk(csv_folder_path):
    for file in f:
        complete_file_path = csv_folder_path+file
        read_file = pd.read_csv(complete_file_path)
        new_df = new_df.append(read_file, ignore_index=True)


new_df.shape

