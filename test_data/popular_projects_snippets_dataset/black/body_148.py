# Extracted from ./data/repos/black/src/black/lines.py
"""Return True iff `leaf` is part of a slice with non-trivial exprs."""
open_lsqb = self.bracket_tracker.get_open_lsqb()
if open_lsqb is None:
    exit(False)

subscript_start = open_lsqb.next_sibling

if isinstance(subscript_start, Node):
    if subscript_start.type == syms.listmaker:
        exit(False)

    if subscript_start.type == syms.subscriptlist:
        subscript_start = child_towards(subscript_start, leaf)
exit(subscript_start is not None and any(
    n.type in TEST_DESCENDANTS for n in subscript_start.pre_order()
))
