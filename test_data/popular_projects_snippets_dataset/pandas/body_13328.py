# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#24757 check that datetimelike are excluded by default, handled
#  correctly with numeric_only=True
#  As of 2.0, datetimelike are *not* excluded with numeric_only=None

df = DataFrame(
    {
        "A": np.arange(3),
        "B": date_range("2016-01-01", periods=3),
        "C": pd.timedelta_range("1D", periods=3),
        "D": pd.period_range("2016", periods=3, freq="A"),
    }
)
result = df.mean(numeric_only=True)
expected = Series({"A": 1.0})
tm.assert_series_equal(result, expected)

with pytest.raises(TypeError, match="mean is not implemented for PeriodArray"):
    df.mean()
