# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
left = DataFrame(
    {
        "id": list("abcde"),
        "v1": np.random.randn(5),
        "v2": np.random.randn(5),
        "dummy": list("abcde"),
        "v3": np.random.randn(5),
    },
    columns=["id", "v1", "v2", "dummy", "v3"],
)
right = DataFrame(
    {
        "id": ["a", "b", np.nan, np.nan, np.nan],
        "sv3": [1.234, 5.678, np.nan, np.nan, np.nan],
    }
)

result = merge(left, right, on="id", how="left")

rdf = right.drop(["id"], axis=1)
expected = left.join(rdf)
tm.assert_frame_equal(result, expected)
