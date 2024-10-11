# Extracted from ./data/repos/flask/src/flask/sessions.py
raise RuntimeError(
    "The session is unavailable because no secret "
    "key was set.  Set the secret_key on the "
    "application to something unique and secret."
)
