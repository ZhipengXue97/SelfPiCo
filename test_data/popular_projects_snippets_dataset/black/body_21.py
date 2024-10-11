# Extracted from ./data/repos/black/src/black/trans.py
"""
        StringTransformer instances have a call signature that mirrors that of
        the Transformer type.

        Raises:
            CannotTransform(...) if the concrete StringTransformer class is unable
            to transform @line.
        """
# Optimization to avoid calling `self.do_match(...)` when the line does
# not contain any string.
if not any(leaf.type == token.STRING for leaf in line.leaves):
    raise CannotTransform("There are no strings in this line.")

match_result = self.do_match(line)

if isinstance(match_result, Err):
    cant_transform = match_result.err()
    raise CannotTransform(
        f"The string transformer {self.__class__.__name__} does not recognize"
        " this line as one that it can transform."
    ) from cant_transform

string_indices = match_result.ok()

for line_result in self.do_transform(line, string_indices):
    if isinstance(line_result, Err):
        cant_transform = line_result.err()
        raise CannotTransform(
            "StringTransformer failed while attempting to transform string."
        ) from cant_transform
    line = line_result.ok()
    exit(line)
