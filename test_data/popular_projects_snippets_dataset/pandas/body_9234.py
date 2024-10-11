# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
parser = all_parsers
data = """\
year,month,day,hour,minute,second,a,b
2001,01,05,10,00,0,0.0,10.
2001,01,5,10,0,00,1.,11.
"""
result = parser.read_csv_check_warnings(
    warn,
    "use 'date_format' instead",
    StringIO(data),
    header=0,
    parse_dates={"ymdHMS": [0, 1, 2, 3, 4, 5]},
    **{key: value},
)
expected = DataFrame(
    [
        [datetime(2001, 1, 5, 10, 0, 0), 0.0, 10.0],
        [datetime(2001, 1, 5, 10, 0, 0), 1.0, 11.0],
    ],
    columns=["ymdHMS", "a", "b"],
)
tm.assert_frame_equal(result, expected)
