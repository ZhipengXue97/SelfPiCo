# Extracted from https://stackoverflow.com/questions/20845213/how-to-avoid-pandas-creating-an-index-in-a-saved-csv
df.set_index('timestamp')
df.to_csv('processed.csv')

pd.read_csv('processed.csv', index_col='timestamp')

pd.read_csv('filename.csv')
pd.set_index('column_name')

