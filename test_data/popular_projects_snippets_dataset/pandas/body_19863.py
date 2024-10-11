# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# no longer do integer div for any ops, but deal with the 0's
dtype2 = any_real_numpy_dtype

first = Series([3, 4, 5, 8], name="first").astype(dtype1)
second = Series([0, 0, 0, 3], name="second").astype(dtype2)

with np.errstate(all="ignore"):
    expected = Series(
        first.values.astype(np.float64) / second.values,
        dtype="float64",
        name=None,
    )
expected.iloc[0:3] = np.inf
if first.dtype == "int64" and second.dtype == "float32":
    # when using numexpr, the casting rules are slightly different
    # and int64/float32 combo results in float32 instead of float64
    if expr.USE_NUMEXPR and switch_numexpr_min_elements == 0:
        expected = expected.astype("float32")

result = first / second
tm.assert_series_equal(result, expected)
assert not result.equals(second / first)
