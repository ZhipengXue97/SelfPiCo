# Extracted from ./data/repos/pandas/pandas/tests/apply/test_str.py
# GH 35964
if op == "ngroup":
    request.node.add_marker(
        pytest.mark.xfail(raises=ValueError, reason="ngroup not valid for NDFrame")
    )
args = [0.0] if op == "fillna" else []
ones = np.ones(string_series.shape[0])
expected = string_series.groupby(ones).transform(op, *args)
result = string_series.transform(op, 0, *args)
tm.assert_series_equal(result, expected)
