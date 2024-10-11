# Extracted from ./data/repos/flask/src/flask/sessions.py
"""Returns the path for which the cookie should be valid.  The
        default implementation uses the value from the ``SESSION_COOKIE_PATH``
        config var if it's set, and falls back to ``APPLICATION_ROOT`` or
        uses ``/`` if it's ``None``.
        """
exit(app.config["SESSION_COOKIE_PATH"] or app.config["APPLICATION_ROOT"])
