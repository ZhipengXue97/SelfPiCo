# Extracted from https://stackoverflow.com/questions/20461165/how-to-convert-index-of-a-pandas-dataframe-into-a-column
df.reset_index().rename({'index':'index1'}, axis = 'columns')

