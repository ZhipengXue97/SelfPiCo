# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_astype.py
# with missing values
arr = pd.array([True, False, None], dtype="boolean")

with pytest.raises(ValueError, match="cannot convert NA to integer"):
    arr.astype("int64")

with pytest.raises(ValueError, match="cannot convert float NaN to"):
    arr.astype("bool")

result = arr.astype("float64")
expected = np.array([1, 0, np.nan], dtype="float64")
tm.assert_numpy_array_equal(result, expected)

result = arr.astype("str")
expected = np.array(["True", "False", "<NA>"], dtype=f"{tm.ENDIAN}U5")
tm.assert_numpy_array_equal(result, expected)

# no missing values
arr = pd.array([True, False, True], dtype="boolean")
result = arr.astype("int64")
expected = np.array([1, 0, 1], dtype="int64")
tm.assert_numpy_array_equal(result, expected)

result = arr.astype("bool")
expected = np.array([True, False, True], dtype="bool")
tm.assert_numpy_array_equal(result, expected)
