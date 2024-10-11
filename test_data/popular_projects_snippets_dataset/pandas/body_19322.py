# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
obj = frame_or_series(
    [1, 2, 3],
    index=[Timestamp("2016"), Timestamp("2019"), Timestamp("2017")],
)
with pytest.raises(
    KeyError, match="Value based partial slicing on non-monotonic"
):
    obj.loc[start:"2022"]
