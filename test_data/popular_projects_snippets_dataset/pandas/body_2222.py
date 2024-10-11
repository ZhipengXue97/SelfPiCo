# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        First discrete difference of element.

        Calculates the difference of each element compared with another
        element in the group (default is element in previous row).

        Parameters
        ----------
        periods : int, default 1
            Periods to shift for calculating difference, accepts negative values.
        axis : axis to shift, default 0
            Take difference over rows (0) or columns (1).

            .. deprecated:: 2.1.0
                For axis=1, operate on the underlying object instead. Otherwise
                the axis keyword is not necessary.

        Returns
        -------
        Series or DataFrame
            First differences.
        %(see_also)s
        Examples
        --------
        For SeriesGroupBy:

        >>> lst = ['a', 'a', 'a', 'b', 'b', 'b']
        >>> ser = pd.Series([7, 2, 8, 4, 3, 3], index=lst)
        >>> ser
        a     7
        a     2
        a     8
        b     4
        b     3
        b     3
        dtype: int64
        >>> ser.groupby(level=0).diff()
        a    NaN
        a   -5.0
        a    6.0
        b    NaN
        b   -1.0
        b    0.0
        dtype: float64

        For DataFrameGroupBy:

        >>> data = {'a': [1, 3, 5, 7, 7, 8, 3], 'b': [1, 4, 8, 4, 4, 2, 1]}
        >>> df = pd.DataFrame(data, index=['dog', 'dog', 'dog',
        ...                   'mouse', 'mouse', 'mouse', 'mouse'])
        >>> df
                 a  b
          dog    1  1
          dog    3  4
          dog    5  8
        mouse    7  4
        mouse    7  4
        mouse    8  2
        mouse    3  1
        >>> df.groupby(level=0).diff()
                 a    b
          dog  NaN  NaN
          dog  2.0  3.0
          dog  2.0  4.0
        mouse  NaN  NaN
        mouse  0.0  0.0
        mouse  1.0 -2.0
        mouse -5.0 -1.0
        """
if axis is not lib.no_default:
    axis = self.obj._get_axis_number(axis)
    self._deprecate_axis(axis, "diff")
else:
    axis = 0

if axis != 0:
    exit(self.apply(lambda x: x.diff(periods=periods, axis=axis)))

obj = self._obj_with_exclusions
shifted = self.shift(periods=periods)

# GH45562 - to retain existing behavior and match behavior of Series.diff(),
# int8 and int16 are coerced to float32 rather than float64.
dtypes_to_f32 = ["int8", "int16"]
if obj.ndim == 1:
    if obj.dtype in dtypes_to_f32:
        shifted = shifted.astype("float32")
else:
    to_coerce = [c for c, dtype in obj.dtypes.items() if dtype in dtypes_to_f32]
    if len(to_coerce):
        shifted = shifted.astype({c: "float32" for c in to_coerce})

exit(obj - shifted)
