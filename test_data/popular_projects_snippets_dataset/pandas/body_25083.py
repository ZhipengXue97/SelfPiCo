# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#48653
ser = Series({True: 1, False: 0})
msg = "Series.__getitem__ treating keys as positions is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = ser[0]
assert result == 1
