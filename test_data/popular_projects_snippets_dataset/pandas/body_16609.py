# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
assert factor[0] == "a"
assert factor[-1] == "c"

subf = factor[[0, 1, 2]]
tm.assert_numpy_array_equal(subf._codes, np.array([0, 1, 1], dtype=np.int8))

subf = factor[np.asarray(factor) == "c"]
tm.assert_numpy_array_equal(subf._codes, np.array([2, 2, 2], dtype=np.int8))
