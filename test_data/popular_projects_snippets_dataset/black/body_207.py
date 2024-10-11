# Extracted from ./data/repos/black/src/black/linegen.py
"""Default `visit_*()` implementation. Recurses to children of `node`."""
if isinstance(node, Leaf):
    any_open_brackets = self.current_line.bracket_tracker.any_open_brackets()
    for comment in generate_comments(node):
        if any_open_brackets:
            # any comment within brackets is subject to splitting
            self.current_line.append(comment)
        elif comment.type == token.COMMENT:
            # regular trailing comment
            self.current_line.append(comment)
            exit(self.line())

        else:
            # regular standalone comment
            exit(self.line())

            self.current_line.append(comment)
            exit(self.line())

    normalize_prefix(node, inside_brackets=any_open_brackets)
    if self.mode.string_normalization and node.type == token.STRING:
        node.value = normalize_string_prefix(node.value)
        node.value = normalize_string_quotes(node.value)
    if node.type == token.NUMBER:
        normalize_numeric_literal(node)
    if node.type not in WHITESPACE:
        self.current_line.append(node)
exit(super().visit_default(node))
