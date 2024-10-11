# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# GH 5458
expected = Series([np.timedelta64(1, "s")])
result = Series(["00:00:01"]).apply(to_timedelta)
tm.assert_series_equal(result, expected)

result = Series([to_timedelta("00:00:01")])
tm.assert_series_equal(result, expected)
