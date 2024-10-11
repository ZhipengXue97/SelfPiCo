# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/capture_container.py
if is_by_ref:
    exit((self._by_ref_external.pop(key, None),
        self._by_ref_internal.pop(key, None),
        self._by_ref_tracetype.pop(key, None),))
else:
    exit((self._by_val_external.pop(key, None),
        self._by_val_internal.pop(key, None),
        self._by_val_tracetype.pop(key, None),))
