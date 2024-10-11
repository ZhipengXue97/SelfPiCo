# Extracted from https://stackoverflow.com/questions/12555323/how-to-add-a-new-column-to-an-existing-dataframe
df1['e'] = np.random.randn(sLength)

df1['e'] = df1['a'].map(lambda x: np.random.random())

