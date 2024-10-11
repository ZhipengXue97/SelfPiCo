# Extracted from https://stackoverflow.com/questions/19384532/get-statistics-for-each-group-such-as-count-mean-etc-using-pandas-groupby
agg_df = df.pivot_table(
    values=['col3', 'col4', 'col5'], 
    index=['col1', 'col2'], 
    aggfunc=['size', 'mean', 'median']
).reset_index()
# flatten the MultiIndex column (should be omitted if MultiIndex is preferred)
agg_df.columns = [i if not j else f"{j}_{i}" for i,j in agg_df.columns]

aggfuncs = {f'{c}_{f}': (c, f) for c in ['col3', 'col4', 'col5'] for f in ['mean', 'count']}
agg_df = df.groupby(['col1', 'col2'], as_index=False).agg(**aggfuncs)

agg_df = df.groupby(['col1', 'col2'], as_index=False).agg(col3_mean=('col3', 'mean'), col4_median=('col4', 'median'), col5_min=('col5', 'min'))
# or equivalently,
agg_df = df.groupby(['col1', 'col2'], as_index=False).agg(**{'_'.join(p): p for p in [('col3', 'mean'), ('col4', 'median'), ('col5', 'min')]})

