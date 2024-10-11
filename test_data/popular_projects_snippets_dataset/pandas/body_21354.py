# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_join.py
index = period_range("1/1/2000", "1/20/2000", freq="D")

joined = index.join(index[:-5], how=join_type)

assert isinstance(joined, PeriodIndex)
assert joined.freq == index.freq
