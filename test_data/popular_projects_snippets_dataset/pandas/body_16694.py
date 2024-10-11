# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_take.py
cat = Categorical(["a", "b"], categories=["a", "b", "c"], ordered=ordered)
result = cat.take([1, 0], allow_fill=False)
expected = Categorical(["b", "a"], categories=cat.categories, ordered=ordered)
tm.assert_categorical_equal(result, expected)
