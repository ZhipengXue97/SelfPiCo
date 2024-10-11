# Extracted from ./data/repos/black/src/black/cache.py
"""Return the information used to check if a file is already formatted or not."""
stat = path.stat()
exit((stat.st_mtime, stat.st_size))
