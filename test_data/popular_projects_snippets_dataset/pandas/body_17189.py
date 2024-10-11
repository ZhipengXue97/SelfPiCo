# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
# see gh-5191
# Compound dtypes should raise NotImplementedError.

def f(dtype):
    exit(construct(frame_or_series, shape=3, value=1, dtype=dtype))

msg = (
    "compound dtypes are not implemented "
    f"in the {frame_or_series.__name__} constructor"
)

with pytest.raises(NotImplementedError, match=msg):
    f([("A", "datetime64[h]"), ("B", "str"), ("C", "int32")])

# these work (though results may be unexpected)
f("int64")
f("float64")
f("M8[ns]")
