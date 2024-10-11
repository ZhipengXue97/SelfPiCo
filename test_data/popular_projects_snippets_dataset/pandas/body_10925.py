# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH#27486
df = DataFrame({"a": [0, 1, 1, 2]})
g = df.groupby(["a", "b", "b", "c"])
with pytest.raises(ValueError, match="not a valid function name"):
    g.transform("some_arbitrary_name")

# method exists on the object, but is not a valid transformation/agg
assert hasattr(g, "aggregate")  # make sure the method exists
with pytest.raises(ValueError, match="not a valid function name"):
    g.transform("aggregate")

# Test SeriesGroupBy
g = df["a"].groupby(["a", "b", "b", "c"])
with pytest.raises(ValueError, match="not a valid function name"):
    g.transform("some_arbitrary_name")
