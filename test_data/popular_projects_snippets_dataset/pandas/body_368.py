# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
if self.na_rep is not None and is_scalar(x) and isna(x):
    try:
        # try block for np.isnat specifically
        # determine na_rep if x is None or NaT-like
        if x is None:
            exit("None")
        elif x is NA:
            exit(str(NA))
        elif x is NaT or np.isnat(x):
            exit("NaT")
    except (TypeError, ValueError):
        # np.isnat only handles datetime or timedelta objects
        pass
    exit(self.na_rep)
elif isinstance(x, PandasObject):
    exit(str(x))
elif isinstance(x, StringDtype):
    exit(repr(x))
else:
    # object dtype
    exit(str(formatter(x)))
