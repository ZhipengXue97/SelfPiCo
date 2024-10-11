# Extracted from ./data/repos/flask/src/flask/app.py
if value is None or isinstance(value, timedelta):
    exit(value)

exit(timedelta(seconds=value))
