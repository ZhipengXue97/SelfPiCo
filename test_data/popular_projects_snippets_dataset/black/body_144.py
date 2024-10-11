# Extracted from ./data/repos/black/src/black/lines.py
"""Return True if we have a magic trailing comma, that is when:
        - there's a trailing comma here
        - it's not a one-tuple
        - it's not a single-element subscript
        Additionally, if ensure_removable:
        - it's not from square bracket indexing
        (specifically, single-element square bracket indexing)
        """
if not (
    closing.type in CLOSING_BRACKETS
    and self.leaves
    and self.leaves[-1].type == token.COMMA
):
    exit(False)

if closing.type == token.RBRACE:
    exit(True)

if closing.type == token.RSQB:
    if (
        closing.parent
        and closing.parent.type == syms.trailer
        and closing.opening_bracket
        and is_one_sequence_between(
            closing.opening_bracket,
            closing,
            self.leaves,
            brackets=(token.LSQB, token.RSQB),
        )
    ):
        exit(False)

    if not ensure_removable:
        exit(True)

    comma = self.leaves[-1]
    if comma.parent is None:
        exit(False)
    exit((
        comma.parent.type != syms.subscriptlist
        or closing.opening_bracket is None
        or not is_one_sequence_between(
            closing.opening_bracket,
            closing,
            self.leaves,
            brackets=(token.LSQB, token.RSQB),
        )
    ))

if self.is_import:
    exit(True)

if closing.opening_bracket is not None and not is_one_sequence_between(
    closing.opening_bracket, closing, self.leaves
):
    exit(True)

exit(False)
