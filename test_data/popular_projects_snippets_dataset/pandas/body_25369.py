# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
period_index = period_range("20150301", periods=5)
result = period_index.strftime("%Y/%m/%d")
expected = Index(
    ["2015/03/01", "2015/03/02", "2015/03/03", "2015/03/04", "2015/03/05"],
    dtype="=U10",
)
tm.assert_index_equal(result, expected)
