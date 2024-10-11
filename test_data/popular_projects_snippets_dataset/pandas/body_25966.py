# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
exit(Period(
    year=bound.year,
    month=bound.month,
    day=bound.day,
    hour=bound.hour,
    minute=bound.minute,
    second=bound.second + offset,
    freq="us",
))
