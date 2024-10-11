# Extracted from ./data/repos/black/src/black/debug.py
"""Pretty-print the lib2to3 AST of a given string of `code`.

        Convenience method for debugging.
        """
v: DebugVisitor[None] = DebugVisitor()
if isinstance(code, str):
    code = lib2to3_parse(code)
list(v.visit(code))
