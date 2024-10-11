# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH 51892
df = DataFrame(
    {
        (1, 2): ["a", "b", "c"],
        (1, 3): ["d", "e", "f"],
        (2, 2): ["g", "h", "i"],
        (2, 4): ["j", "k", "l"],
    }
)
with pytest.raises(KeyError, match=r"(1, 4)"):
    df.loc[0, (1, 4)]
