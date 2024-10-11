# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_records.py
# GH#3189
index = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
data = np.zeros((8, 4))
df = DataFrame(data, index=index)
r = df.to_records(index=True)["level_0"]
assert "bar" in r
assert "one" not in r
