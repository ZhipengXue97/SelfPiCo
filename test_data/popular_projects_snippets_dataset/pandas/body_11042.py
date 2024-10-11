# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 13432, unorderable types in py3
df = DataFrame([[0, 1, 2]], columns=["A", "B", 0])
expected = DataFrame([[1, 2]], columns=["B", 0], index=Index([0], name="A"))

result = df.groupby("A").first()
tm.assert_frame_equal(result, expected)

result = df.groupby("A").sum()
tm.assert_frame_equal(result, expected)
