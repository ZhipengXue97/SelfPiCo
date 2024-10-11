# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_filter.py
# GH13101
df = DataFrame({"a": [1, 2], "あ": [3, 4]})

tm.assert_frame_equal(df.filter(like=name), expected)
tm.assert_frame_equal(df.filter(regex=name), expected)
