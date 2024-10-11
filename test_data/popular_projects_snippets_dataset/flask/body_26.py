# Extracted from ./data/repos/flask/src/flask/ctx.py
try:
    exit(self.__dict__[name])
except KeyError:
    raise AttributeError(name) from None
