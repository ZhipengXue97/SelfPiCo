# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
x = Series(pd.PeriodIndex(["2015-11-01", "2015-12-01"], freq="D"))
y = Series(pd.PeriodIndex(["2015-10-01", "2016-01-01"], freq="M"))
expected = Series([x[0], x[1], y[0], y[1]], dtype="object")
result = concat([x, y], ignore_index=True)
tm.assert_series_equal(result, expected)
assert result.dtype == "object"
