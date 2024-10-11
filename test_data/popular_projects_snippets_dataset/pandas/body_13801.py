# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
n = 10
# Cast to object to avoid implicit cast when setting entry to pd.NaT below
df = DataFrame(np.random.randn(n, 3)).astype({0: object})
df["dates1"] = date_range("1/1/2012", periods=n)
df["dates3"] = date_range("1/1/2014", periods=n)
df.iloc[0, 0] = pd.NaT
return_value = df.set_index("dates1", inplace=True, drop=True)
assert return_value is None
res = df.query(
    "(index < 20130101) & (20130101 < dates3)", engine=engine, parser=parser
)
expec = df[(df.index < "20130101") & ("20130101" < df.dates3)]
tm.assert_frame_equal(res, expec)
