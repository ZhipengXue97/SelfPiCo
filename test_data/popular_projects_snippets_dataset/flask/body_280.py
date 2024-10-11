# Extracted from ./data/repos/flask/src/flask/helpers.py
import warnings

warnings.warn(
    "'locked_cached_property' is deprecated and will be removed in Flask 2.4."
    " Use a lock inside the decorated function if locking is needed.",
    DeprecationWarning,
    stacklevel=2,
)
super().__init__(fget, name=name, doc=doc)
self.lock = RLock()
