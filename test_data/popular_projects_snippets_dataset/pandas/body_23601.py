# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_quarter.py
expected = "<QuarterEnd: startingMonth=3>"
assert repr(QuarterEnd()) == expected
expected = "<QuarterEnd: startingMonth=3>"
assert repr(QuarterEnd(startingMonth=3)) == expected
expected = "<QuarterEnd: startingMonth=1>"
assert repr(QuarterEnd(startingMonth=1)) == expected
