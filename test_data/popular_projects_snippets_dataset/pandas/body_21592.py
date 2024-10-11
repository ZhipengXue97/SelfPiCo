# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index(list("ABC"), name="xxx")
msg = (
    "When allow_fill=True and fill_value is not None, "
    "all indices must be >= -1"
)

with pytest.raises(ValueError, match=msg):
    index.take(np.array([1, 0, -2]), fill_value=True)
with pytest.raises(ValueError, match=msg):
    index.take(np.array([1, 0, -5]), fill_value=True)
