# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_constructors.py
pa = pytest.importorskip("pyarrow")

data = []
arr = pa.array(data)
dtype = DatetimeTZDtype(unit=unit, tz=tz)

result = dtype.__from_arrow__(arr)
expected = DatetimeArray(np.array(data, dtype=f"datetime64[{unit}]"))
expected = expected.tz_localize(tz=tz)
tm.assert_extension_array_equal(result, expected)

result = dtype.__from_arrow__(pa.chunked_array([arr]))
tm.assert_extension_array_equal(result, expected)
