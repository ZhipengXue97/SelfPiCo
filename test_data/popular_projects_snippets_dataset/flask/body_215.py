# Extracted from ./data/repos/flask/src/flask/globals.py
import warnings

warnings.warn(
    f"'_{self.name}_ctx_stack' is deprecated and will be removed in Flask 2.4."
    f" Use 'g' to store data, or '{self.name}_ctx' to access the current"
    " context.",
    DeprecationWarning,
    stacklevel=2,
)
exit(self.cv.get(None))
