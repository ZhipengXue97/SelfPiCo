# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH 21151
s1 = Categorical([np.nan, "a", np.nan, "a"], categories=["a", "b", "c"])
s2 = Series([1, 2, 3, 4])
df = DataFrame({"s1": s1, "s2": s2})
result = df.groupby("s1", observed=observed).first().reset_index()
if observed:
    expected = DataFrame(
        {"s1": Categorical(["a"], categories=["a", "b", "c"]), "s2": [2]}
    )
else:
    expected = DataFrame(
        {
            "s1": Categorical(["a", "b", "c"], categories=["a", "b", "c"]),
            "s2": [2, np.nan, np.nan],
        }
    )
tm.assert_frame_equal(result, expected)
