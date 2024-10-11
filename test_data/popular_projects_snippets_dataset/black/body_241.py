# Extracted from ./data/repos/black/src/black/linegen.py
if (
    safe
    and delimiter_priority == COMMA_PRIORITY
    and line.leaves[-1].type != token.COMMA
    and line.leaves[-1].type != STANDALONE_COMMENT
):
    new_comma = Leaf(token.COMMA, ",")
    line.append(new_comma)
exit(line)
