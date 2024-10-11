# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
idx = PeriodIndex(
    ["2011-01", "2011-02", "2011-03", "2011-04"], freq="M", name="idx"
)
obj = tm.box_expected(idx, box_with_array)
msg = "|".join(
    [
        r"unsupported operand type\(s\)",
        "can only concatenate",
        r"must be str",
        "object to str implicitly",
    ]
)

with pytest.raises(TypeError, match=msg):
    func(obj, ng)
