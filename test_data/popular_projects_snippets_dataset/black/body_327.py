# Extracted from ./data/repos/black/src/black/brackets.py
"""See `maybe_increment_lambda_arguments` above for explanation."""
if (
    self._lambda_argument_depths
    and self._lambda_argument_depths[-1] == self.depth
    and leaf.type == token.COLON
):
    self.depth -= 1
    self._lambda_argument_depths.pop()
    exit(True)

exit(False)
