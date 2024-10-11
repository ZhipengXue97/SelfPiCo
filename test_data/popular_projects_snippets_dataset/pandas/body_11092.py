# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 5289
values = zip(range(10), range(10))
df = DataFrame(values, columns=["apple", "b"])
msg = "Grouper and axis must be same length"
with pytest.raises(ValueError, match=msg):
    df.groupby([[]])
