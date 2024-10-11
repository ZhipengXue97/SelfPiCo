# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# GH 9093
ser = Series([1, 2, 3, 4])
ser.index.name = index_name

# default is the ylabel is not shown and xlabel is index name (reverse for barh)
ax = ser.plot(kind=kind)
if kind == "barh":
    assert ax.get_xlabel() == ""
    assert ax.get_ylabel() == old_label
elif kind == "hist":
    assert ax.get_xlabel() == ""
    assert ax.get_ylabel() == "Frequency"
else:
    assert ax.get_ylabel() == ""
    assert ax.get_xlabel() == old_label

# old xlabel will be overridden and assigned ylabel will be used as ylabel
ax = ser.plot(kind=kind, ylabel=new_label, xlabel=new_label)
assert ax.get_ylabel() == new_label
assert ax.get_xlabel() == new_label
