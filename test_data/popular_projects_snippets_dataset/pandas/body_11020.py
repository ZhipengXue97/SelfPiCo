# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 38815
grouped = df.groupby("A")
with pytest.raises(ValueError, match="could not convert"):
    grouped.skew()
