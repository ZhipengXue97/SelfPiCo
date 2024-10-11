# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
# GH#9512
for vals in (
    [0, 1, 0],
    [0, 0, -1],
    [0, -1, -1],
    ["00:01:00", "00:01:00", "00:02:00"],
    ["00:01:00", "00:01:00", "00:00:01"],
):
    idx = TimedeltaIndex(vals)
    assert idx[0] in idx
