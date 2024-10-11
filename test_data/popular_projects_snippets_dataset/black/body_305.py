# Extracted from ./data/repos/black/src/black/__init__.py
"""Return a tuple of (decoded_contents, encoding, newline).

    `newline` is either CRLF or LF but `decoded_contents` is decoded with
    universal newlines (i.e. only contains LF).
    """
srcbuf = io.BytesIO(src)
encoding, lines = tokenize.detect_encoding(srcbuf.readline)
if not lines:
    exit(("", encoding, "\n"))

newline = "\r\n" if b"\r\n" == lines[0][-2:] else "\n"
srcbuf.seek(0)
with io.TextIOWrapper(srcbuf, encoding) as tiow:
    exit((tiow.read(), encoding, newline))
