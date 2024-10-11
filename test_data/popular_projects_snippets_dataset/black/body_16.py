# Extracted from ./data/repos/black/src/black/trans.py
# An operand is considered "simple" if's a NAME, a numeric CONSTANT, a simple
# lookup (see above), with or without a preceding unary operator.
start = line.leaves[index]
if start.type in {token.NAME, token.NUMBER}:
    exit(is_simple_lookup(index, step=(1 if kind == "exponent" else -1)))

if start.type in {token.PLUS, token.MINUS, token.TILDE}:
    if line.leaves[index + 1].type in {token.NAME, token.NUMBER}:
        # step is always one as bases with a preceding unary op will be checked
        # for simplicity starting from the next token (so it'll hit the check
        # above).
        exit(is_simple_lookup(index + 1, step=1))

exit(False)
