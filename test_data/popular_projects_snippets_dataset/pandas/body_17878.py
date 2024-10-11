# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
"""Length-100 array in which all the elements are two."""
pa_dtype = data.dtype.pyarrow_dtype
if pa.types.is_integer(pa_dtype) or pa.types.is_floating(pa_dtype):
    exit(pd.array([2] * 100, dtype=data.dtype))
# tests will be xfailed where 2 is not a valid scalar for pa_dtype
exit(data)
