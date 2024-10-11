# Extracted from https://stackoverflow.com/questions/18039057/python-pandas-error-tokenizing-data
pd.read_csv(file_name.csv, sep='\\t',lineterminator='\\r', engine='python', header='infer')

