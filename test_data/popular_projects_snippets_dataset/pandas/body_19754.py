# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
idx = PeriodIndex(
    ["2011-01-01", "2011-02-01", "2011-03-01", "2011-04-01"],
    freq="D",
    name="idx",
)
f = lambda x: x + pd.offsets.Day()
exp = PeriodIndex(
    ["2011-01-02", "2011-02-02", "2011-03-02", "2011-04-02"],
    freq="D",
    name="idx",
)
self._check(idx, f, exp)

f = lambda x: x + pd.offsets.Day(2)
exp = PeriodIndex(
    ["2011-01-03", "2011-02-03", "2011-03-03", "2011-04-03"],
    freq="D",
    name="idx",
)
self._check(idx, f, exp)

f = lambda x: x - pd.offsets.Day(2)
exp = PeriodIndex(
    ["2010-12-30", "2011-01-30", "2011-02-27", "2011-03-30"],
    freq="D",
    name="idx",
)
self._check(idx, f, exp)
