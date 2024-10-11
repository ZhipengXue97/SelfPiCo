# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
if not index_flat.is_unique:
    pytest.skip("Randomly generated index_flat was not unique.")
index = index_flat

# test copy.union(subset) - need sort for unicode and string
first = index.copy().set_names(fname)
second = index[1:].set_names(sname)
union = first.union(second).sort_values()
expected = index.set_names(expected_name).sort_values()
tm.assert_index_equal(union, expected)
