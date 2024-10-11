# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
df = uint64_frame
idx = df["A"].rename("foo")

# setitem
assert "C" not in df.columns
df["C"] = idx
tm.assert_series_equal(df["C"], Series(idx, name="C"))

assert "D" not in df.columns
df["D"] = "foo"
df["D"] = idx
tm.assert_series_equal(df["D"], Series(idx, name="D"))
del df["D"]

# With NaN: because uint64 has no NaN element,
# the column should be cast to object.
df2 = df.copy()
df2.iloc[1, 1] = pd.NaT
df2.iloc[1, 2] = pd.NaT
result = df2["B"]
tm.assert_series_equal(notna(result), Series([True, False, True], name="B"))
tm.assert_series_equal(
    df2.dtypes,
    Series(
        [np.dtype("uint64"), np.dtype("O"), np.dtype("O")],
        index=["A", "B", "C"],
    ),
)
