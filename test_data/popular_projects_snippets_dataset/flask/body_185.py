# Extracted from ./data/repos/flask/src/flask/scaffold.py
"""Used by :func:`send_file` to determine the ``max_age`` cache
        value for a given file path if it wasn't passed.

        By default, this returns :data:`SEND_FILE_MAX_AGE_DEFAULT` from
        the configuration of :data:`~flask.current_app`. This defaults
        to ``None``, which tells the browser to use conditional requests
        instead of a timed cache, which is usually preferable.

        .. versionchanged:: 2.0
            The default configuration is ``None`` instead of 12 hours.

        .. versionadded:: 0.9
        """
value = current_app.config["SEND_FILE_MAX_AGE_DEFAULT"]

if value is None:
    exit(None)

if isinstance(value, timedelta):
    exit(int(value.total_seconds()))

exit(value)
