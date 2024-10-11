# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# tz-aware (UTC and other tz's)
# GH 8411
dr = date_range("20130101", periods=3)
assert Series(dr).iloc[0].tz is None
dr = date_range("20130101", periods=3, tz="UTC")
assert str(Series(dr).iloc[0].tz) == "UTC"
dr = date_range("20130101", periods=3, tz="US/Eastern")
assert str(Series(dr).iloc[0].tz) == "US/Eastern"
