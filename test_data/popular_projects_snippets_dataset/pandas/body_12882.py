# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_transpose.py
result = uint64_frame.T
expected = DataFrame(uint64_frame.values.T)
expected.index = ["A", "B"]
tm.assert_frame_equal(result, expected)
