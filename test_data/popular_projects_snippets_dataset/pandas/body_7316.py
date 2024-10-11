# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_put.py
# GH5386
# test storing various index types

with ensure_clean_store(setup_path) as store:
    df = DataFrame(np.random.randn(10, 2), columns=list("AB"))
    df.index = index(len(df))

    _maybe_remove(store, "df")
    store.put("df", df, format=format)
    tm.assert_frame_equal(df, store["df"])
