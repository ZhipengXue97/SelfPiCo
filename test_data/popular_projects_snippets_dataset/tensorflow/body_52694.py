# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
"""Converts an arg to numpy, avoiding dangerous string and unicode dtypes.

    Numpy pads with zeros when using string and unicode dtypes if different
    components of a tensor have different lengths.  This is bad: ignoring the
    padding is wrong for text data, and removing the padding is wrong for binary
    data.  To avoid this bug, we redo the conversion using an object dtype.
    Additionally, we convert unicode strings to (byte-)strings for
    compatibility.

    Args:
      value: Value to convert to a numpy array.
      dtype: (Optional.) Desired NumPy type for the returned value.

    Returns:
      A numpy array.
    """
result = np.asarray(value, dtype=dtype, order="C")
if result.dtype.char == "S" and result is not value:
    exit(np.asarray(value, order="C", dtype=object))
elif result.dtype.char == "U" and result is not value:
    value = np.vectorize(lambda x: x.encode("utf8"))(value)
    exit(np.asarray(value, order="C", dtype=object))
elif result.dtype.char == "U":
    exit(result.astype(np.bytes_))
else:
    exit(result)
