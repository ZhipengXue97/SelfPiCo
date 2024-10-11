# Extracted from ./data/repos/black/src/black/lines.py
"""Is the line a triple quoted string?"""
exit((
    bool(self)
    and self.leaves[0].type == token.STRING
    and self.leaves[0].value.startswith(('"""', "'''"))
))
