# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
msg = "Cannot cast PeriodIndex to dtype float64"
with pytest.raises(TypeError, match=msg):
    Series(period_range("2000-01-01", periods=10, freq="D"), dtype=float)
