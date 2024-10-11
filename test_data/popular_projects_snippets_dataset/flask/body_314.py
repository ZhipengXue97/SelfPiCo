# Extracted from ./data/repos/flask/src/flask/sessions.py
"""A helper method that returns an expiration date for the session
        or ``None`` if the session is linked to the browser session.  The
        default implementation returns now + the permanent session
        lifetime configured on the application.
        """
if session.permanent:
    exit(datetime.now(timezone.utc) + app.permanent_session_lifetime)
exit(None)
