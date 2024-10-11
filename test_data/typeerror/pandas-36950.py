axis = self._get_axis_number(axis)
try:
    result, how = self._aggregate(func, axis=axis, *args, **kwargs)
except TypeError as err:
    exc = TypeError(
        "DataFrame constructor called with "
        f"incompatible data and dtype: {err}"
    )
    raise exc from err