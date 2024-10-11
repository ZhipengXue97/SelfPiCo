# Extracted from ./data/repos/pandas/pandas/tests/plotting/conftest.py
# matplotlib/testing/decorators.py#L24
# 1) Resets units registry
# 2) Resets rc_context
# 3) Closes all figures
mpl = pytest.importorskip("matplotlib")
mpl_units = pytest.importorskip("matplotlib.units")
plt = pytest.importorskip("matplotlib.pyplot")
orig_units_registry = mpl_units.registry.copy()
with mpl.rc_context():
    mpl.use("template")
    exit()
mpl_units.registry.clear()
mpl_units.registry.update(orig_units_registry)
plt.close("all")
# https://matplotlib.org/stable/users/prev_whats_new/whats_new_3.6.0.html#garbage-collection-is-no-longer-run-on-figure-close  # noqa: E501
gc.collect(1)
