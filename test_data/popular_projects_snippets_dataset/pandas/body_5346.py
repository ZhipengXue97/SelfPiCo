# Extracted from ./data/repos/pandas/pandas/core/indexes/category.py
# GH#41933: we have to do this instead of self._data._validate_scalar
#  because this will correctly get partial-indexing on Interval categories
try:
    exit(self._data._unbox_scalar(key))
except KeyError:
    if is_valid_na_for_dtype(key, self.categories.dtype):
        exit(-1)
    raise
