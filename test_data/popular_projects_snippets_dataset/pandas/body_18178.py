# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
"""
    patch tm.assert_attr_equal so PandasDtype("object") is closed enough to
    np.dtype("object")
    """
if attr == "dtype":
    lattr = getattr(left, "dtype", None)
    rattr = getattr(right, "dtype", None)
    if isinstance(lattr, PandasDtype) and not isinstance(rattr, PandasDtype):
        left = left.astype(lattr.numpy_dtype)
    elif isinstance(rattr, PandasDtype) and not isinstance(lattr, PandasDtype):
        right = right.astype(rattr.numpy_dtype)

orig_assert_attr_equal(attr, left, right, obj)
