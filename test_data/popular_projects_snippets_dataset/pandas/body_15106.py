# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append_common.py
# GH 13524

# category + not-category => not-category
s1 = Series([1, 2, np.nan], dtype="category")
s2 = Series([2, 1, 2])

exp = Series([1, 2, np.nan, 2, 1, 2], dtype=np.float64)
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)

# result shouldn't be affected by 1st elem dtype
exp = Series([2, 1, 2, 1, 2, np.nan], dtype=np.float64)
tm.assert_series_equal(pd.concat([s2, s1], ignore_index=True), exp)
tm.assert_series_equal(s2._append(s1, ignore_index=True), exp)

# all values are not in category => not-category
s1 = Series([3, 2], dtype="category")
s2 = Series([2, 1])

exp = Series([3, 2, 2, 1])
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)

exp = Series([2, 1, 3, 2])
tm.assert_series_equal(pd.concat([s2, s1], ignore_index=True), exp)
tm.assert_series_equal(s2._append(s1, ignore_index=True), exp)

# completely different categories => not-category
s1 = Series([10, 11, np.nan], dtype="category")
s2 = Series([1, 3, 2])

exp = Series([10, 11, np.nan, 1, 3, 2], dtype=np.float64)
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)

exp = Series([1, 3, 2, 10, 11, np.nan], dtype=np.float64)
tm.assert_series_equal(pd.concat([s2, s1], ignore_index=True), exp)
tm.assert_series_equal(s2._append(s1, ignore_index=True), exp)

# different dtype => not-category
s1 = Series([10, 11, np.nan], dtype="category")
s2 = Series(["a", "b", "c"])

exp = Series([10, 11, np.nan, "a", "b", "c"])
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)

exp = Series(["a", "b", "c", 10, 11, np.nan])
tm.assert_series_equal(pd.concat([s2, s1], ignore_index=True), exp)
tm.assert_series_equal(s2._append(s1, ignore_index=True), exp)

# if normal series only contains NaN-likes => not-category
s1 = Series([10, 11], dtype="category")
s2 = Series([np.nan, np.nan, np.nan])

exp = Series([10, 11, np.nan, np.nan, np.nan])
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)

exp = Series([np.nan, np.nan, np.nan, 10, 11])
tm.assert_series_equal(pd.concat([s2, s1], ignore_index=True), exp)
tm.assert_series_equal(s2._append(s1, ignore_index=True), exp)
