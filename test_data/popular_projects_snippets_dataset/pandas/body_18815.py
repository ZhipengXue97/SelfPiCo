# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
df = DataFrame(
    np.random.randn(3, 3),
    columns=[[2, 2, 4], [6, 8, 10]],
    index=[[4, 4, 8], [8, 10, 12]],
)
expected = df.iloc[[0, 1]].droplevel(0)
result = df.loc[4]
tm.assert_frame_equal(result, expected)
