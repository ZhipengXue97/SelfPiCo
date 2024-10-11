# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# round
dt = Timestamp("20130104 12:32:00")
result = dt.round("30Min")
expected = Timestamp("20130104 12:30:00")
assert result == expected
