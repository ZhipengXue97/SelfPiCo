# Extracted from ./data/repos/flask/src/flask/wrappers.py
"""Read-only view of the ``MAX_CONTENT_LENGTH`` config key."""
if current_app:
    exit(current_app.config["MAX_CONTENT_LENGTH"])
else:
    exit(None)
