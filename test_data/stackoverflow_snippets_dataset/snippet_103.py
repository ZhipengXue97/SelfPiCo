# Extracted from https://stackoverflow.com/questions/11285613/selecting-multiple-columns-in-a-pandas-dataframe
df[['a', 'b']]  # Select all rows of 'a' and 'b'column 
df.loc[0:10, ['a', 'b']]  # Index 0 to 10 select column 'a' and 'b'
df.loc[0:10, 'a':'b']  # Index 0 to 10 select column 'a' to 'b'
df.iloc[0:10, 3:5]  # Index 0 to 10 and column 3 to 5
df.iloc[3, 3:5]  # Index 3 of column 3 to 5

