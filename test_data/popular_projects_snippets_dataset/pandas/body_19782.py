# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#22074
# reversion test that we _don't_ call _assert_tzawareness_compat
# when comparing against TimedeltaIndex
dti = date_range("2000-01-01", periods=10, tz="Asia/Tokyo")

result = dti == other
expected = np.array([False] * 10)
tm.assert_numpy_array_equal(result, expected)

result = dti != other
expected = np.array([True] * 10)
tm.assert_numpy_array_equal(result, expected)
msg = "Invalid comparison between"
with pytest.raises(TypeError, match=msg):
    dti < other
with pytest.raises(TypeError, match=msg):
    dti <= other
with pytest.raises(TypeError, match=msg):
    dti > other
with pytest.raises(TypeError, match=msg):
    dti >= other
