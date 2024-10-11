# Extracted from https://stackoverflow.com/questions/26266362/how-do-i-count-the-nan-values-in-a-column-in-pandas-dataframe
df.isnull().sum().sort_values(ascending = False)

df.isnull().sum().sort_values(ascending = False).head(15)

