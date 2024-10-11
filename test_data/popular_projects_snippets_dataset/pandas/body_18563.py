# Extracted from ./data/repos/pandas/pandas/tests/extension/base/missing.py
ser = pd.Series(data_missing)
result = ser.dropna()
expected = ser.iloc[[1]]
self.assert_series_equal(result, expected)
