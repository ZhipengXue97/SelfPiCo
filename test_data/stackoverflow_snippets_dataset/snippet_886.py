# Extracted from https://stackoverflow.com/questions/25351968/how-can-i-display-full-non-truncated-dataframe-information-in-html-when-conver
import pandas as pd
import dask.dataframe as dd
pd.set_option('display.max_colwidth', -1) # This will set the no truncate for Pandas as well as for Dask. I am not sure how it does for Dask though, but it works.

train_data = dd.read_csv('./data/train.csv')
train_data.head(5)

