# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
_, ax = mpl.pyplot.subplots()
sample_points = np.linspace(-100, 100, 20)
ax = ts.plot.kde(logy=True, bw_method=0.5, ind=sample_points, ax=ax)
_check_ax_scales(ax, yaxis="log")
_check_text_labels(ax.yaxis.get_label(), "Density")
