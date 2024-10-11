# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_read_fwf.py
data = """
To be skipped
Not  To  Be  Skipped
Once more to be skipped
123  34   8      123
456  78   9      456
""".strip()
skiprows = [0, 2]
expected = read_csv(StringIO(data), skiprows=skiprows, delim_whitespace=True)

result = read_fwf(StringIO(data), skiprows=skiprows)
tm.assert_frame_equal(result, expected)
