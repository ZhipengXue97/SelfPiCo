# Extracted from ./data/repos/pandas/pandas/core/indexing.py
# GH#5567 this will fail if the label is not present in the axis.
exit(self.obj.xs(label, axis=axis))
