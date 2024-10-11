# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
# GH#50643
df = DataFrame({"a": [1, 2, 3]})
expected = df.copy()
result = df.sort_values(by=[], inplace=True)
tm.assert_frame_equal(df, expected)
assert result is None
