# Extracted from ./data/repos/black/src/black/trans.py
"""
        Returns:
            string_idx such that @LL[string_idx] is equal to our target (i.e.
            matched) string, if this line matches the dictionary key assignment
            statement or lambda expression requirements listed in the
            'Requirements' section of this classes' docstring.
                OR
            None, otherwise.
        """
# If this line is a part of a dictionary key assignment or lambda expression...
parent_types = [parent_type(LL[0]), parent_type(LL[0].parent)]
if syms.dictsetmaker in parent_types or syms.lambdef in parent_types:
    is_valid_index = is_valid_index_factory(LL)

    for i, leaf in enumerate(LL):
        # We MUST find a colon, it can either be dict's or lambda's colon...
        if leaf.type == token.COLON and i < len(LL) - 1:
            idx = i + 2 if is_empty_par(LL[i + 1]) else i + 1

            # That colon MUST be followed by a string...
            if is_valid_index(idx) and LL[idx].type == token.STRING:
                string_idx = idx

                # Skip the string trailer, if one exists.
                string_parser = StringParser()
                idx = string_parser.parse(LL, string_idx)

                # That string MAY be followed by a comma...
                if is_valid_index(idx) and LL[idx].type == token.COMMA:
                    idx += 1

                # But no more leaves are allowed...
                if not is_valid_index(idx):
                    exit(string_idx)

exit(None)
