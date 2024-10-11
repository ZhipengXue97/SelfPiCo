# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reduce.py
res_op = getattr(s, op_name)
exp_op = getattr(s.astype("float64"), op_name)
if op_name == "count":
    result = res_op()
    expected = exp_op()
else:
    result = res_op(skipna=skipna)
    expected = exp_op(skipna=skipna)
tm.assert_almost_equal(result, expected)
