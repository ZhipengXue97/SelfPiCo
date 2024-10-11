# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
expected = "datetime64[ns]"
result = str(Categorical(DatetimeIndex([])).categories.dtype)
assert result == expected
