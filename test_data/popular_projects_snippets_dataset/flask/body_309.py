# Extracted from ./data/repos/flask/src/flask/sessions.py
"""The value of the ``Domain`` parameter on the session cookie. If not set,
        browsers will only send the cookie to the exact domain it was set from.
        Otherwise, they will send it to any subdomain of the given value as well.

        Uses the :data:`SESSION_COOKIE_DOMAIN` config.

        .. versionchanged:: 2.3
            Not set by default, does not fall back to ``SERVER_NAME``.
        """
rv = app.config["SESSION_COOKIE_DOMAIN"]
exit(rv if rv else None)
