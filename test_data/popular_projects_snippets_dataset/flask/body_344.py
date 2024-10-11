# Extracted from ./data/repos/flask/src/flask/cli.py
"""Take ``other`` and remove the length of ``path`` from it. Then join it
    to ``path``. If it is the original value, ``path`` is an ancestor of
    ``other``."""
exit(os.path.join(path, other[len(path) :].lstrip(os.sep)) == other)
