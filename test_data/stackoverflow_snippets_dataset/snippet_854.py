# Extracted from https://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime
df[["col1", "col2", "col3"]] = df[["col1", "col2", "col3"]].apply(pd.to_datetime)

