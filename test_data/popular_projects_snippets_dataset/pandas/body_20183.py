# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# unicode
index = MultiIndex.from_tuples(
    [
        ("\u03b1", 0),
        ("\u03b1", 1),
        ("\u03b2", 2),
        ("\u03b2", 3),
        ("\u03b3", 4),
        ("\u03b3", 5),
        ("\u03b4", 6),
        ("\u03b4", 7),
    ],
    names=["i0", "i1"],
)
columns = MultiIndex.from_tuples(
    [("bar", "\u0394"), ("bar", "\u0395")], names=["c0", "c1"]
)
df = DataFrame(np.random.randint(0, 10, (8, 2)), columns=columns, index=index)
_check_plot_works(df.plot, title="\u03A3")
