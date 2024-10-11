# Extracted from ./data/repos/black/src/black/parsing.py
filename = "<unknown>"
exit(ast.parse(
    src, filename, feature_version=version, type_comments=type_comments
))
