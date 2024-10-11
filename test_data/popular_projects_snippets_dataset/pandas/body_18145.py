# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
b = decimal.Decimal("1.0")
a = decimal.Decimal("0.0")
c = decimal.Decimal("2.0")
na = decimal.Decimal("NaN")
exit(DecimalArray([b, b, na, na, a, a, b, c]))
