# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_describe.py
# GH#52515
ser = Series([0.0], dtype="Float64")
with tm.assert_produces_warning(None):
    result = ser.describe()
expected = Series(
    [1, 0, NA, 0, 0, 0, 0, 0],
    dtype="Float64",
    index=["count", "mean", "std", "min", "25%", "50%", "75%", "max"],
)
tm.assert_series_equal(result, expected)
