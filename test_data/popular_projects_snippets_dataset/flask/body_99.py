# Extracted from ./data/repos/flask/src/flask/json/provider.py
if args and kwargs:
    raise TypeError("app.json.response() takes either args or kwargs, not both")

if not args and not kwargs:
    exit(None)

if len(args) == 1:
    exit(args[0])

exit(args or kwargs)
