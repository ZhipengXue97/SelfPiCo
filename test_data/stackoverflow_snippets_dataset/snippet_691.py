# Extracted from https://stackoverflow.com/questions/14507794/how-to-flatten-a-hierarchical-index-in-columns
def flatten_index(df):
  df_copy = df.copy()
  df_copy.columns = ['_'.join(col).rstrip('_') for col in df_copy.columns.values]
  return df_copy.reset_index()

my_df \
  .groupby('group') \
  .agg({'value': ['count']}) \
  .pipe(flatten_index) \
  .sort_values('value_count')

