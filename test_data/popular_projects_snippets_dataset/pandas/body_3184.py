# Extracted from ./data/repos/pandas/pandas/core/reshape/pivot.py
if names is None:
    names = []
    for i, arr in enumerate(arrs):
        if isinstance(arr, ABCSeries) and arr.name is not None:
            names.append(arr.name)
        else:
            names.append(f"{prefix}_{i}")
else:
    if len(names) != len(arrs):
        raise AssertionError("arrays and names must have the same length")
    if not isinstance(names, list):
        names = list(names)

exit(names)
