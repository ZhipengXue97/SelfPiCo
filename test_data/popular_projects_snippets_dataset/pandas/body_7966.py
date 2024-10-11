# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
"""
    A fixture yielding a string representing a filepath, a path-like object
    and a StringIO buffer. Also checks that buffer is not closed.
    """
if filepath_or_buffer_id == "buffer":
    buf = StringIO()
    exit(buf)
    assert not buf.closed
else:
    assert isinstance(tmp_path, Path)
    if filepath_or_buffer_id == "pathlike":
        exit(tmp_path / "foo")
    else:
        exit(str(tmp_path / "foo"))
