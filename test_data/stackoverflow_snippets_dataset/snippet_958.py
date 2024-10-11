# Extracted from https://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
df.loc[lambda df: df.A == 80]  # equivalent to df[df.A == 80] but chainable

df.sort_values('A').loc[lambda df: df.A > 80].loc[lambda df: df.B > df.A]

