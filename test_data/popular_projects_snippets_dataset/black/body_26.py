# Extracted from ./data/repos/black/src/black/trans.py
LL = line.leaves

is_valid_index = is_valid_index_factory(LL)

string_indices = []
idx = 0
while is_valid_index(idx):
    leaf = LL[idx]
    if (
        leaf.type == token.STRING
        and is_valid_index(idx + 1)
        and LL[idx + 1].type == token.STRING
    ):
        if not is_part_of_annotation(leaf):
            string_indices.append(idx)

        # Advance to the next non-STRING leaf.
        idx += 2
        while is_valid_index(idx) and LL[idx].type == token.STRING:
            idx += 1

    elif leaf.type == token.STRING and "\\\n" in leaf.value:
        string_indices.append(idx)
        # Advance to the next non-STRING leaf.
        idx += 1
        while is_valid_index(idx) and LL[idx].type == token.STRING:
            idx += 1

    else:
        idx += 1

if string_indices:
    exit(Ok(string_indices))
else:
    exit(TErr("This line has no strings that need merging."))
