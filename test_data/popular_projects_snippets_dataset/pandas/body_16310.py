# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_function.py
arr = pd.array([1, 2, 3, None], dtype=dtype)
result = arr.sum(skipna=skipna, min_count=min_count)
if skipna and min_count == 0:
    assert result == 6.0
else:
    assert result is pd.NA
