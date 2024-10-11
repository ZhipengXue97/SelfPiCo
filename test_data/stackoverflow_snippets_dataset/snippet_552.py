# Extracted from https://stackoverflow.com/questions/19828822/how-to-check-whether-a-pandas-dataframe-is-empty
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10000, 4), columns=list('ABCD'))

def empty(df):
    return df.empty

def lenz(df):
    return len(df) == 0

def lenzi(df):
    return len(df.index) == 0

'''
%timeit empty(df)
%timeit lenz(df)
%timeit lenzi(df)

10000 loops, best of 3: 13.9 µs per loop
100000 loops, best of 3: 2.34 µs per loop
1000000 loops, best of 3: 695 ns per loop

len on index seems to be faster
'''

