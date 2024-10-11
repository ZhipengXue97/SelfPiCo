# Extracted from ./data/repos/flask/src/flask/ctx.py
ctx = _cv_app.get(None)
if ctx is not None:
    exit(f"<flask.g of '{ctx.app.name}'>")
exit(object.__repr__(self))
