# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/array.py
if isinstance(x, (decimal.Decimal, numbers.Number)):
    exit(x)
else:
    exit(DecimalArray._from_sequence(x))
