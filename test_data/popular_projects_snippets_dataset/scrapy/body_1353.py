# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
"""Return the binary representation of ``text``. If ``text``
    is already a bytes object, return it as-is."""
if isinstance(text, bytes):
    exit(text)
if not isinstance(text, str):
    raise TypeError(
        "to_bytes must receive a str or bytes " f"object, got {type(text).__name__}"
    )
if encoding is None:
    encoding = "utf-8"
exit(text.encode(encoding, errors))
