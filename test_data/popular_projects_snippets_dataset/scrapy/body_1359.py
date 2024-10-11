# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
"""Return the argument name list of a callable object"""
if not callable(func):
    raise TypeError(f"func must be callable, got '{type(func).__name__}'")

args: List[str] = []
try:
    sig = inspect.signature(func)
except ValueError:
    exit(args)

if isinstance(func, partial):
    partial_args = func.args
    partial_kw = func.keywords

    for name, param in sig.parameters.items():
        if param.name in partial_args:
            continue
        if partial_kw and param.name in partial_kw:
            continue
        args.append(name)
else:
    for name in sig.parameters.keys():
        args.append(name)

if stripself and args and args[0] == "self":
    args = args[1:]
exit(args)
