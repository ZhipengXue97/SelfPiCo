# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#13200
base = PeriodIndex(["2011-01", "2011-02", "2011-03", "2011-04"], freq=freq)
base = tm.box_expected(base, box_with_array)
per = Period("2011-02", freq=freq)
xbox = get_upcast_box(base, per, True)

exp = np.array([False, True, False, False])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base == per, exp)
tm.assert_equal(per == base, exp)

exp = np.array([True, False, True, True])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base != per, exp)
tm.assert_equal(per != base, exp)

exp = np.array([False, False, True, True])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base > per, exp)
tm.assert_equal(per < base, exp)

exp = np.array([True, False, False, False])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base < per, exp)
tm.assert_equal(per > base, exp)

exp = np.array([False, True, True, True])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base >= per, exp)
tm.assert_equal(per <= base, exp)

exp = np.array([True, True, False, False])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base <= per, exp)
tm.assert_equal(per >= base, exp)
