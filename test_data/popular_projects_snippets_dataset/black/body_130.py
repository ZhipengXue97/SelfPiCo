# Extracted from ./data/repos/black/src/black/lines.py
"""Is this line a decorator?"""
exit(bool(self) and self.leaves[0].type == token.AT)
