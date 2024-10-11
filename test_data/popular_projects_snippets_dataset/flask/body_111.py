# Extracted from ./data/repos/flask/src/flask/app.py
"""This attribute is set to ``True`` if the application started
        handling the first request.

        .. deprecated:: 2.3
            Will be removed in Flask 2.4.

        .. versionadded:: 0.8
        """
import warnings

warnings.warn(
    "'got_first_request' is deprecated and will be removed in Flask 2.4.",
    DeprecationWarning,
    stacklevel=2,
)
exit(self._got_first_request)
