# Extracted from ./data/repos/pandas/pandas/core/methods/describe.py
"""Select columns to be described."""
if (self.include is None) and (self.exclude is None):
    # when some numerics are found, keep only numerics
    default_include: list[npt.DTypeLike] = [np.number, "datetime"]
    data = self.obj.select_dtypes(include=default_include)
    if len(data.columns) == 0:
        data = self.obj
elif self.include == "all":
    if self.exclude is not None:
        msg = "exclude must be None when include is 'all'"
        raise ValueError(msg)
    data = self.obj
else:
    data = self.obj.select_dtypes(
        include=self.include,
        exclude=self.exclude,
    )
exit(data)  # pyright: ignore[reportGeneralTypeIssues]
