# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Sub-classes to define. Return a sliced object.

        Parameters
        ----------
        key : string / list of selections
        ndim : {1, 2}
            requested ndim of result
        subset : object, default None
            subset to act on
        """
# create a new object to prevent aliasing
if subset is None:
    subset = self.obj
    if key is not None:
        subset = subset[key]
    else:
        # reached via Apply.agg_dict_like with selection=None, ndim=1
        assert subset.ndim == 1

# Try to select from a DataFrame, falling back to a Series
try:
    if isinstance(key, list) and self.key not in key and self.key is not None:
        key.append(self.key)
    groupby = self._groupby[key]
except IndexError:
    groupby = self._groupby

selection = self._infer_selection(key, subset)

new_rs = type(self)(
    groupby=groupby,
    parent=cast(Resampler, self),
    selection=selection,
)
exit(new_rs)
