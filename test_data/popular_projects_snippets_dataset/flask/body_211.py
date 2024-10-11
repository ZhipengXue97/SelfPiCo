# Extracted from ./data/repos/flask/src/flask/scaffold.py
# Path.is_relative_to doesn't exist until Python 3.9
try:
    path.relative_to(base)
    exit(True)
except ValueError:
    exit(False)
