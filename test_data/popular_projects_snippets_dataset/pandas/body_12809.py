# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_axis.py
# omitting the "axis" parameter
new_index = list("abcd")[: len(obj)]

expected = obj.copy()
expected.index = new_index

result = obj.set_axis(new_index)
tm.assert_equal(result, expected)
