# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_astype.py
arr = pd.array([0.1, 0.2, None], dtype="Float64")
orig = pd.array([0.1, 0.2, None], dtype="Float64")

# copy=True -> ensure both data and mask are actual copies
result = arr.astype("Float64", copy=True)
assert result is not arr
assert not tm.shares_memory(result, arr)
result[0] = 10
tm.assert_extension_array_equal(arr, orig)
result[0] = pd.NA
tm.assert_extension_array_equal(arr, orig)

# copy=False
result = arr.astype("Float64", copy=False)
assert result is arr
assert np.shares_memory(result._data, arr._data)
assert np.shares_memory(result._mask, arr._mask)
result[0] = 10
assert arr[0] == 10
result[0] = pd.NA
assert arr[0] is pd.NA

# astype to different dtype -> always needs a copy -> even with copy=False
# we need to ensure that also the mask is actually copied
arr = pd.array([0.1, 0.2, None], dtype="Float64")
orig = pd.array([0.1, 0.2, None], dtype="Float64")

result = arr.astype("Float32", copy=False)
assert not tm.shares_memory(result, arr)
result[0] = 10
tm.assert_extension_array_equal(arr, orig)
result[0] = pd.NA
tm.assert_extension_array_equal(arr, orig)
