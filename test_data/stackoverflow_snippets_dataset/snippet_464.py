# Extracted from https://stackoverflow.com/questions/16729574/how-can-i-get-a-value-from-a-cell-of-a-dataframe
df_gdp.columns

df_gdp[df_gdp["Country Code"] == "USA"]["1996"].values[0]

