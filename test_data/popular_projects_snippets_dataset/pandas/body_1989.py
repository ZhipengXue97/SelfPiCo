# Extracted from ./data/repos/pandas/pandas/core/tools/datetimes.py
"""
    Properly boxes the ndarray of datetimes to DatetimeIndex
    if it is possible or to generic Index instead

    Parameters
    ----------
    dt_array: 1-d array
        Array of datetimes to be wrapped in an Index.
    utc : bool
        Whether to convert/localize timestamps to UTC.
    name : string, default None
        Name for a resulting index

    Returns
    -------
    result : datetime of converted dates
        - DatetimeIndex if convertible to sole datetime64 type
        - general Index otherwise
    """

if lib.is_np_dtype(dt_array.dtype, "M"):
    tz = "utc" if utc else None
    exit(DatetimeIndex(dt_array, tz=tz, name=name))
exit(Index(dt_array, name=name, dtype=dt_array.dtype))
