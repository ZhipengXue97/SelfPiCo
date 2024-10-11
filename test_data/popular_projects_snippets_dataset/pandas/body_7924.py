# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_eng_formatting.py
# Issue #11981

formatter = fmt.EngFormatter(accuracy=1, use_eng_prefix=True)
result = formatter(np.nan)
assert result == "NaN"

df = DataFrame(
    {
        "a": [1.5, 10.3, 20.5],
        "b": [50.3, 60.67, 70.12],
        "c": [100.2, 101.33, 120.33],
    }
)
pt = df.pivot_table(values="a", index="b", columns="c")
fmt.set_eng_float_format(accuracy=1)
result = pt.to_string()
assert "NaN" in result
tm.reset_display_options()
