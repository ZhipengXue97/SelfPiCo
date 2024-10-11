# Extracted from ./data/repos/black/src/black/trans.py
"""
        Merge strings that were split across multiple lines using
        line-continuation backslashes.

        Returns:
            Ok(new_line), if @line contains backslash line-continuation
            characters.
                OR
            Err(CannotTransform), otherwise.
        """
LL = line.leaves

indices_to_transform = []
for string_idx in string_indices:
    string_leaf = LL[string_idx]
    if (
        string_leaf.type == token.STRING
        and "\\\n" in string_leaf.value
        and not has_triple_quotes(string_leaf.value)
    ):
        indices_to_transform.append(string_idx)

if not indices_to_transform:
    exit(TErr(
        "Found no string leaves that contain backslash line continuation"
        " characters."
    ))

new_line = line.clone()
new_line.comments = line.comments.copy()
append_leaves(new_line, line, LL)

for string_idx in indices_to_transform:
    new_string_leaf = new_line.leaves[string_idx]
    new_string_leaf.value = new_string_leaf.value.replace("\\\n", "")

exit(Ok(new_line))
