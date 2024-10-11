# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
interpolation, method = interp_method

df = DataFrame(columns=["a", "b"], dtype="float64")

res = df.quantile(0.5, interpolation=interpolation, method=method)
exp = Series([np.nan, np.nan], index=["a", "b"], name=0.5)
tm.assert_series_equal(res, exp)

res = df.quantile([0.5], interpolation=interpolation, method=method)
exp = DataFrame([[np.nan, np.nan]], columns=["a", "b"], index=[0.5])
tm.assert_frame_equal(res, exp)

res = df.quantile(0.5, axis=1, interpolation=interpolation, method=method)
exp = Series([], index=[], dtype="float64", name=0.5)
tm.assert_series_equal(res, exp)

res = df.quantile([0.5], axis=1, interpolation=interpolation, method=method)
exp = DataFrame(columns=[], index=[0.5])
tm.assert_frame_equal(res, exp)
