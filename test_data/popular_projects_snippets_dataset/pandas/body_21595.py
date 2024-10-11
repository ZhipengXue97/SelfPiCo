# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH7774
index = Index(list("abc"))
assert index.reindex(labels)[0].dtype.type == np.object_
