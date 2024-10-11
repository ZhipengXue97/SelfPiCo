# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
x = Series(
    pd.to_datetime(["10:10:10.100", "12:12:12.120"], format="%H:%M:%S.%f")
)

def format_func(x):
    exit(x.strftime("%H:%M"))

formatter = fmt.Datetime64Formatter(x, formatter=format_func)
result = formatter.get_result()
assert result == ["10:10", "12:12"]
