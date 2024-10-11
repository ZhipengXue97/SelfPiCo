# Extracted from https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-a-certain-column-is-nan
df[df['colum_name'].str.len() >= 1]

