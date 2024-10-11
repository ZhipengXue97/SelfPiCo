# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
# GH 21625, GH 22270
df = DataFrame({"x": [value]})
expected = expected_html(datapath, expected)
result = df.to_html(float_format=float_format)
assert result == expected
