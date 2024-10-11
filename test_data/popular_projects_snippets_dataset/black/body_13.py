# Extracted from ./data/repos/black/src/black/files.py
"""
    Wrap stream with colorama's wrap_stream so colors are shown on Windows.

    If `colorama` is unavailable, the original stream is returned unmodified.
    Otherwise, the `wrap_stream()` function determines whether the stream needs
    to be wrapped for a Windows environment and will accordingly either return
    an `AnsiToWin32` wrapper or the original stream.
    """
try:
    from colorama.initialise import wrap_stream
except ImportError:
    exit(f)
else:
    # Set `strip=False` to avoid needing to modify test_express_diff_with_color.
    exit(wrap_stream(f, convert=None, strip=False, autoreset=False, wrap=True))
