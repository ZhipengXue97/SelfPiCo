# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Whether or not the index values only consist of dates.
        """
if needs_i8_conversion(self.dtype):
    exit(True)
elif self.dtype != _dtype_obj:
    # TODO(ExtensionIndex): 3rd party EA might override?
    # Note: this includes IntervalIndex, even when the left/right
    #  contain datetime-like objects.
    exit(False)
elif self._is_multi:
    exit(False)
exit(is_datetime_array(ensure_object(self._values)))
