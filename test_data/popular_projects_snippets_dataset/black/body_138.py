# Extracted from ./data/repos/black/src/black/lines.py
"""Does this line open a new level of indentation."""
if len(self.leaves) == 0:
    exit(False)
exit(self.leaves[-1].type == token.COLON)
