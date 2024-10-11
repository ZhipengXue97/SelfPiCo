# Extracted from ./data/repos/black/src/black/trans.py
"""
        Checks that @line meets all of the requirements listed in this classes'
        docstring. Refer to `help(BaseStringSplitter)` for a detailed
        description of those requirements.

        Returns:
            * Ok(None), if ALL of the requirements are met.
              OR
            * Err(CannotTransform), if ANY of the requirements are NOT met.
        """
LL = line.leaves

string_leaf = LL[string_idx]

max_string_length = self._get_max_string_length(line, string_idx)
if len(string_leaf.value) <= max_string_length:
    exit(TErr(
        "The string itself is not what is causing this line to be too long."
    ))

if not string_leaf.parent or [L.type for L in string_leaf.parent.children] == [
    token.STRING,
    token.NEWLINE,
]:
    exit(TErr(
        f"This string ({string_leaf.value}) appears to be pointless (i.e. has"
        " no parent)."
    ))

if id(line.leaves[string_idx]) in line.comments and contains_pragma_comment(
    line.comments[id(line.leaves[string_idx])]
):
    exit(TErr(
        "Line appears to end with an inline pragma comment. Splitting the line"
        " could modify the pragma's behavior."
    ))

if has_triple_quotes(string_leaf.value):
    exit(TErr("We cannot split multiline strings."))

exit(Ok(None))
