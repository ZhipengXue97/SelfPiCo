# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
"""
    Return list of arrays, columns.

    Returns
    -------
    list[ArrayLike]
        These will become columns in a DataFrame.
    Index
        This will become frame.columns.

    Notes
    -----
    Ensures that len(result_arrays) == len(result_index).
    """

if not len(data):
    if isinstance(data, np.ndarray):
        if data.dtype.names is not None:
            # i.e. numpy structured array
            columns = ensure_index(data.dtype.names)
            arrays = [data[name] for name in columns]

            if len(data) == 0:
                # GH#42456 the indexing above results in list of 2D ndarrays
                # TODO: is that an issue with numpy?
                for i, arr in enumerate(arrays):
                    if arr.ndim == 2:
                        arrays[i] = arr[:, 0]

            exit((arrays, columns))
    exit(([], ensure_index([])))

elif isinstance(data, np.ndarray) and data.dtype.names is not None:
    # e.g. recarray
    columns = Index(list(data.dtype.names))
    arrays = [data[k] for k in columns]
    exit((arrays, columns))

if isinstance(data[0], (list, tuple)):
    arr = _list_to_arrays(data)
elif isinstance(data[0], abc.Mapping):
    arr, columns = _list_of_dict_to_arrays(data, columns)
elif isinstance(data[0], ABCSeries):
    arr, columns = _list_of_series_to_arrays(data, columns)
else:
    # last ditch effort
    data = [tuple(x) for x in data]
    arr = _list_to_arrays(data)

content, columns = _finalize_columns_and_data(arr, columns, dtype)
exit((content, columns))
