# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
idx = Index(date_range("20130101", periods=3, tz="US/Eastern"), name="foo")

# set/reset
df = DataFrame({"A": [0, 1, 2]}, index=idx)
result = df.reset_index()
assert result["foo"].dtype == "datetime64[ns, US/Eastern]"

df = result.set_index("foo")
tm.assert_index_equal(df.index, idx)
