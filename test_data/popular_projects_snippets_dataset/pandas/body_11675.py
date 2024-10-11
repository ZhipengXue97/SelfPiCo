# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_numba.py
labels = ["a", "a", "b", "b", "a"]
data = Series([1.0, 2.0, 3.0, 4.0, 5.0])
grouped = data.groupby(labels)
agg_kwargs["engine"] = "numba"
result = grouped.agg(**agg_kwargs)
agg_kwargs["engine"] = "cython"
expected = grouped.agg(**agg_kwargs)
if isinstance(expected, DataFrame):
    tm.assert_frame_equal(result, expected)
else:
    tm.assert_series_equal(result, expected)
