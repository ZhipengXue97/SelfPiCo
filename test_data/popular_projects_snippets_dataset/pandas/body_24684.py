# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# Test that replaced values are not replaced again
# GH #50778
ser = pd.Series([1, 2, 3])
expected = pd.Series([2, 3, 4])

res = ser.replace([1, 2, 3], [2, 3, 4], inplace=inplace)
if inplace:
    tm.assert_series_equal(ser, expected)
else:
    tm.assert_series_equal(res, expected)
