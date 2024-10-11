# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index([1, 2, 3])
dropped = index.drop(key, errors="ignore")

tm.assert_index_equal(dropped, expected)
