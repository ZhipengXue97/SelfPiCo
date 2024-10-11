# Extracted from ./data/repos/black/src/black/__init__.py
"""If notebook is marked as non-Python, don't format it.

    All notebook metadata fields are optional, see
    https://nbformat.readthedocs.io/en/latest/format_description.html. So
    if a notebook has empty metadata, we will try to parse it anyway.
    """
language = nb.get("metadata", {}).get("language_info", {}).get("name", None)
if language is not None and language != "python":
    raise NothingChanged from None
