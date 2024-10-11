# Extracted from ./data/repos/flask/src/flask/sessions.py
"""Used by session backends to determine if a ``Set-Cookie`` header
        should be set for this session cookie for this response. If the session
        has been modified, the cookie is set. If the session is permanent and
        the ``SESSION_REFRESH_EACH_REQUEST`` config is true, the cookie is
        always set.

        This check is usually skipped if the session was deleted.

        .. versionadded:: 0.11
        """

exit(session.modified or (
    session.permanent and app.config["SESSION_REFRESH_EACH_REQUEST"]
))
