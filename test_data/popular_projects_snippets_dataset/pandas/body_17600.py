# Extracted from ./data/repos/pandas/pandas/tests/copy_view/index/test_index.py
ser = Series([1, 2])
idx = Index(ser, copy=True)  # noqa: F841
arr = get_array(ser)
ser.iloc[0] = 100
assert np.shares_memory(get_array(ser), arr)
