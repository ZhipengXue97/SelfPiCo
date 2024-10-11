# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_dataframe.py
# GH#42092 we may want to change this to return object, but that
#  would need a deprecation
df1 = DataFrame(Series([True, False, True, True], dtype="bool"))
df2 = DataFrame(Series([1, 0, 1], dtype="int64"))

result = concat([df1, df2])
expected = concat([df1.astype("int64"), df2])
tm.assert_frame_equal(result, expected)
