# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
op = all_arithmetic_functions
series = tm.makeTimeSeries().rename("ts")
other = func(series)
compare_op(series, other, op)
