# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_numba.py
func, kwargs = numba_supported_reductions
df = DataFrame({"a": [3, 2, 3, 2], "b": range(4), "c": range(1, 5)})
engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}
gb = df.groupby("a", sort=sort)
result = getattr(gb, func)(
    engine="numba", engine_kwargs=engine_kwargs, **kwargs
)
expected = getattr(gb, func)(**kwargs)
tm.assert_frame_equal(result, expected)
