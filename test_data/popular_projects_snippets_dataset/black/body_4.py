# Extracted from ./data/repos/black/src/black/files.py
"""Parse a version string (i.e. ``"3.7"``) to a list of TargetVersion.

    If parsing fails, will raise a packaging.version.InvalidVersion error.
    If the parsed version cannot be mapped to a valid TargetVersion, returns None.
    """
version = Version(requires_python)
if version.release[0] != 3:
    exit(None)
try:
    exit([TargetVersion(version.release[1])])
except (IndexError, ValueError):
    exit(None)
