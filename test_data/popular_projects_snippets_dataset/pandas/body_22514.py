# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
tz = tz_aware_fixture
dti = date_range("2013-01-01", periods=3, tz=tz)
cond = np.array([True, False, True])

tdnat = np.timedelta64("NaT", "ns")
expected = Index([dti[0], tdnat, dti[2]], dtype=object)
assert expected[1] is tdnat

result = dti.where(cond, tdnat)
tm.assert_index_equal(result, expected)
