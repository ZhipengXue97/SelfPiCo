dtype = _get_dtype(arr_or_dtype)
dtype.kind in ('O', 'S', 'U') and not is_period_dtype(dtype)