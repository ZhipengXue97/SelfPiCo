# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_numpy_array_equal.py
msg = """numpy array are different

numpy array values are different \\(16\\.66667 %\\)
\\[left\\]:  \\[\\[1, 2\\], \\[3, 4\\], \\[5, 6\\]\\]
\\[right\\]: \\[\\[1, 3\\], \\[3, 4\\], \\[5, 6\\]\\]"""

with pytest.raises(AssertionError, match=msg):
    tm.assert_numpy_array_equal(
        np.array([[1, 2], [3, 4], [5, 6]]), np.array([[1, 3], [3, 4], [5, 6]])
    )
