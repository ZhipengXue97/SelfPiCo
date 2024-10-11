# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
result = index.astype("category")
expected = CategoricalIndex(index.values)
tm.assert_index_equal(result, expected)

result = index.astype(CategoricalDtype())
tm.assert_index_equal(result, expected)

# non-default params
categories = index.dropna().unique().values[:-1]
dtype = CategoricalDtype(categories=categories, ordered=True)
result = index.astype(dtype)
expected = CategoricalIndex(index.values, categories=categories, ordered=True)
tm.assert_index_equal(result, expected)
