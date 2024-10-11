# Extracted from https://stackoverflow.com/questions/29763620/how-to-select-all-columns-except-one-in-pandas
df[[i for i in list(df.columns) if i not in [list_of_columns_to_exclude]]]

df.loc[:,[i for i in list(df.columns) if i not in [list_of_columns_to_exclude]]]

