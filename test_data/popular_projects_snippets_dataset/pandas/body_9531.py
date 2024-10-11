# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# ENH 20768
# Ensure index=False omits the index from the written Parquet file.
df = pd.DataFrame({"a": [1, 2, 3], "b": ["q", "r", "s"]})

write_kwargs = {"compression": None, "index": False}

# Because we're dropping the index, we expect the loaded dataframe to
# have the default integer index.
expected = df.reset_index(drop=True)

check_round_trip(df, engine, write_kwargs=write_kwargs, expected=expected)

# Ignore custom index
df = pd.DataFrame(
    {"a": [1, 2, 3], "b": ["q", "r", "s"]}, index=["zyx", "wvu", "tsr"]
)

check_round_trip(df, engine, write_kwargs=write_kwargs, expected=expected)

# Ignore multi-indexes as well.
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
df = pd.DataFrame(
    {"one": list(range(8)), "two": [-i for i in range(8)]}, index=arrays
)

expected = df.reset_index(drop=True)
check_round_trip(df, engine, write_kwargs=write_kwargs, expected=expected)
