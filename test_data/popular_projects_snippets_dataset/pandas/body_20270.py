# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
s = Series([1, 2])
ax = s.plot()
assert ax.get_legend() is None

ax = s.plot(legend=True)
assert ax.get_legend().get_texts()[0].get_text() == ""
