# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_setops.py
other = Index([2**63, 2**63 + 5, 2**63 + 10, 2**63 + 15, 2**63 + 20])
result = index_large.intersection(other)
expected = Index(np.sort(np.intersect1d(index_large.values, other.values)))
tm.assert_index_equal(result, expected)

result = other.intersection(index_large)
expected = Index(
    np.sort(np.asarray(np.intersect1d(index_large.values, other.values)))
)
tm.assert_index_equal(result, expected)
