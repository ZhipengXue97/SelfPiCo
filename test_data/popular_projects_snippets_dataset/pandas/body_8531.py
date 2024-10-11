# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
df = DataFrame(
    [[1, 2], [3, 4]],
    columns=pd.MultiIndex.from_arrays(columns),
)
data = StringIO(df.to_json(orient="split"))
result = read_json(data, orient="split")
tm.assert_frame_equal(result, df)
