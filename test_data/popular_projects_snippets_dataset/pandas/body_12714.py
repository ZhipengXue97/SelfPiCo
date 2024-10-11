# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_at_time.py
index = date_range("2012-01-01", "2012-01-05", freq="30min")
df = DataFrame(np.random.randn(len(index), 5), index=index)
akey = time(12, 0, 0)
ainds = [24, 72, 120, 168]

result = df.at_time(akey)
expected = df.loc[akey]
expected2 = df.iloc[ainds]
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result, expected2)
assert len(result) == 4
