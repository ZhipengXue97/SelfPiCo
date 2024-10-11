# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
array = pa.array([1.5, 2.5], type=pa.float64())
with pytest.raises(pa.ArrowInvalid, match="Float value 1.5 was truncated"):
    array.to_pandas(types_mapper={pa.float64(): ArrowDtype(pa.int64())}.get)
