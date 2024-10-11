# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
test_sers = gen_series_formatting()
with option_context("display.max_rows", 4, "display.show_dimensions", False):
    res = repr(test_sers["onel"])
    exp = "0     a\n1     a\n     ..\n98    a\n99    a\ndtype: object"
    assert exp == res
    res = repr(test_sers["twol"])
    exp = "0     ab\n1     ab\n      ..\n98    ab\n99    ab\ndtype: object"
    assert exp == res
    res = repr(test_sers["asc"])
    exp = (
        "0         a\n1        ab\n      ...  \n4     abcde\n5    "
        "abcdef\ndtype: object"
    )
    assert exp == res
    res = repr(test_sers["desc"])
    exp = (
        "5    abcdef\n4     abcde\n      ...  \n1        ab\n0         "
        "a\ndtype: object"
    )
    assert exp == res
