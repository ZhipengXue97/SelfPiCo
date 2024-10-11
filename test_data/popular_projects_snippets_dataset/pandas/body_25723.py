# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
s = Series(data, dtype=any_string_dtype)
result = s.str.split(pat=pat, n=1)
tm.assert_series_equal(expected, result, check_index_type=False)
