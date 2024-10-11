# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
# GH#13496

frame = DataFrame(
    np.arange(16).reshape(4, 4),
    index=[1, 2, 3, 4],
    columns=["A", "B", "C", "D"],
)

# axis=0 : sort rows by index labels
unordered = frame.loc[[3, 2, 4, 1]]
result = unordered.sort_index(axis=0)
expected = frame
tm.assert_frame_equal(result, expected)

result = unordered.sort_index(ascending=False)
expected = frame[::-1]
tm.assert_frame_equal(result, expected)

# axis=1 : sort columns by column names
unordered = frame.iloc[:, [2, 1, 3, 0]]
result = unordered.sort_index(axis=1)
tm.assert_frame_equal(result, frame)

result = unordered.sort_index(axis=1, ascending=False)
expected = frame.iloc[:, ::-1]
tm.assert_frame_equal(result, expected)
