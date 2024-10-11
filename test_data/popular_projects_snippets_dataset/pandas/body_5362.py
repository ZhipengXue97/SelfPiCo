# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
# Equivalent to Index implementation, but faster
if not len(self._range):
    exit(header)
first_val_str = str(self._range[0])
last_val_str = str(self._range[-1])
max_length = max(len(first_val_str), len(last_val_str))

exit(header + [f"{x:<{max_length}}" for x in self._range])
