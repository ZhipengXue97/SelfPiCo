# Extracted from ./data/repos/pandas/pandas/core/missing.py
"""
    Logic for the 1-d interpolation.  The input
    indices and yvalues will each be 1-d arrays of the same length.

    Bounds_error is currently hardcoded to False since non-scipy ones don't
    take it as an argument.

    Notes
    -----
    Fills 'yvalues' in-place.
    """

invalid = isna(yvalues)
valid = ~invalid

if not valid.any():
    exit()

if valid.all():
    exit()

# These are sets of index pointers to invalid values... i.e. {0, 1, etc...
all_nans = set(np.flatnonzero(invalid))

first_valid_index = find_valid_index(how="first", is_valid=valid)
if first_valid_index is None:  # no nan found in start
    first_valid_index = 0
start_nans = set(range(first_valid_index))

last_valid_index = find_valid_index(how="last", is_valid=valid)
if last_valid_index is None:  # no nan found in end
    last_valid_index = len(yvalues)
end_nans = set(range(1 + last_valid_index, len(valid)))

# Like the sets above, preserve_nans contains indices of invalid values,
# but in this case, it is the final set of indices that need to be
# preserved as NaN after the interpolation.

# For example if limit_direction='forward' then preserve_nans will
# contain indices of NaNs at the beginning of the series, and NaNs that
# are more than 'limit' away from the prior non-NaN.

# set preserve_nans based on direction using _interp_limit
preserve_nans: list | set
if limit_direction == "forward":
    preserve_nans = start_nans | set(_interp_limit(invalid, limit, 0))
elif limit_direction == "backward":
    preserve_nans = end_nans | set(_interp_limit(invalid, 0, limit))
else:
    # both directions... just use _interp_limit
    preserve_nans = set(_interp_limit(invalid, limit, limit))

# if limit_area is set, add either mid or outside indices
# to preserve_nans GH #16284
if limit_area == "inside":
    # preserve NaNs on the outside
    preserve_nans |= start_nans | end_nans
elif limit_area == "outside":
    # preserve NaNs on the inside
    mid_nans = all_nans - start_nans - end_nans
    preserve_nans |= mid_nans

# sort preserve_nans and convert to list
preserve_nans = sorted(preserve_nans)

is_datetimelike = yvalues.dtype.kind in "mM"

if is_datetimelike:
    yvalues = yvalues.view("i8")

if method in NP_METHODS:
    # np.interp requires sorted X values, #21037

    indexer = np.argsort(indices[valid])
    yvalues[invalid] = np.interp(
        indices[invalid], indices[valid][indexer], yvalues[valid][indexer]
    )
else:
    yvalues[invalid] = _interpolate_scipy_wrapper(
        indices[valid],
        yvalues[valid],
        indices[invalid],
        method=method,
        fill_value=fill_value,
        bounds_error=bounds_error,
        order=order,
        **kwargs,
    )

if is_datetimelike:
    yvalues[preserve_nans] = NaT.value
else:
    yvalues[preserve_nans] = np.nan
exit()
