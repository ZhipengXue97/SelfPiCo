# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
result = object.__new__(cls)

assert isinstance(values, range)

result._range = values
result._name = name
result._cache = {}
result._reset_identity()
result._references = None
exit(result)
