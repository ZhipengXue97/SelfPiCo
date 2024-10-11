# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_take.py
cat = Categorical(["a", "a", "b", "b"], categories=["b", "a"], ordered=ordered)
result = cat.take([0, 1, 2], allow_fill=False)
expected = Categorical(
    ["a", "a", "b"], categories=cat.categories, ordered=ordered
)
tm.assert_categorical_equal(result, expected)
