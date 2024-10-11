# Extracted from ./data/repos/black/src/black/report.py
"""Increment the counter for failed reformatting. Write out a message."""
err(f"error: cannot format {src}: {message}")
self.failure_count += 1
