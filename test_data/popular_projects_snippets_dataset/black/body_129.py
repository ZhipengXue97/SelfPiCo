# Extracted from ./data/repos/black/src/black/lines.py
"""Is this line a standalone comment?"""
exit(len(self.leaves) == 1 and self.leaves[0].type == STANDALONE_COMMENT)
