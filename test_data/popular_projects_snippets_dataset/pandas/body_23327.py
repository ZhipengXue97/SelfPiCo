# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py
# not a valid freq
msg = "passed window foobar is not compatible with a datetimelike index"
with pytest.raises(ValueError, match=msg):
    regular.rolling(window="foobar")
# not a datetimelike index
msg = "window must be an integer"
with pytest.raises(ValueError, match=msg):
    regular.reset_index().rolling(window="foobar")
