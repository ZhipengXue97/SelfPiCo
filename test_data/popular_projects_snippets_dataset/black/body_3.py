# Extracted from ./data/repos/black/src/black/files.py
"""Infer Black's target version from the project metadata in pyproject.toml.

    Supports the PyPA standard format (PEP 621):
    https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#requires-python

    If the target version cannot be inferred, returns None.
    """
project_metadata = pyproject_toml.get("project", {})
requires_python = project_metadata.get("requires-python", None)
if requires_python is not None:
    try:
        exit(parse_req_python_version(requires_python))
    except InvalidVersion:
        pass
    try:
        exit(parse_req_python_specifier(requires_python))
    except (InvalidSpecifier, InvalidVersion):
        pass

exit(None)
