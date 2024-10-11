# Extracted from ./data/repos/black/src/black/lines.py
"""Is this a with_stmt line?"""
exit(bool(self) and is_with_or_async_with_stmt(self.leaves[0]))
