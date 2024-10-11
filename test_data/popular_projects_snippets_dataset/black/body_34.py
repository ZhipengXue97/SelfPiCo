# Extracted from ./data/repos/black/src/black/trans.py
LL = line.leaves

string_and_rpar_indices: List[int] = []
for string_idx in string_indices:
    string_parser = StringParser()
    rpar_idx = string_parser.parse(LL, string_idx)

    should_transform = True
    for leaf in (LL[string_idx - 1], LL[rpar_idx]):
        if line.comments_after(leaf):
            # Should not strip parentheses which have comments attached
            # to them.
            should_transform = False
            break
    if should_transform:
        string_and_rpar_indices.extend((string_idx, rpar_idx))

if string_and_rpar_indices:
    exit(Ok(self._transform_to_new_line(line, string_and_rpar_indices)))
else:
    exit(Err(
        CannotTransform("All string groups have comments attached to them.")
    ))
