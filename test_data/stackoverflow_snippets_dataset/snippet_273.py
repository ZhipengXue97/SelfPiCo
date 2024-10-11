# Extracted from https://stackoverflow.com/questions/18172851/deleting-dataframe-row-in-pandas-based-on-column-value
df[~df.line_race.eq(0)]

