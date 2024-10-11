# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
idx = Index(["a,b", "c,d"], name="xxx")
result = idx.str.partition(",")
expected = MultiIndex.from_tuples([("a", ",", "b"), ("c", ",", "d")])
assert result.nlevels == 3
tm.assert_index_equal(result, expected)
