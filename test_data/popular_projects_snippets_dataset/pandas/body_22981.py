# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 38523, 38787
arrays = [
    ["Falcon", "Falcon", "Parrot", "Parrot"],
    ["Captive", "Wild", "Captive", "Wild"],
]
index = MultiIndex.from_arrays(arrays, names=("Animal", "Type"))
df = DataFrame({"Max Speed": [390.0, 350.0, 30.0, 20.0]}, index=index)
result = df.groupby(level=0)["Max Speed"].rolling(2).sum()
expected = Series(
    [np.nan, 740.0, np.nan, 50.0],
    index=MultiIndex.from_tuples(
        [
            ("Falcon", "Falcon", "Captive"),
            ("Falcon", "Falcon", "Wild"),
            ("Parrot", "Parrot", "Captive"),
            ("Parrot", "Parrot", "Wild"),
        ],
        names=["Animal", "Animal", "Type"],
    ),
    name="Max Speed",
)
tm.assert_series_equal(result, expected)
