# Extracted from ./data/repos/black/src/black/brackets.py
"""In a lambda expression, there might be more than one argument.

        To avoid splitting on the comma in this situation, increase the depth of
        tokens between `lambda` and `:`.
        """
if leaf.type == token.NAME and leaf.value == "lambda":
    self.depth += 1
    self._lambda_argument_depths.append(self.depth)
    exit(True)

exit(False)
