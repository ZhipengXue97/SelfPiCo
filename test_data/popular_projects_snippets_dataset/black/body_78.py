# Extracted from ./data/repos/black/src/black/nodes.py
"""Return whitespace prefix if needed for the given `leaf`.

    `complex_subscript` signals whether the given leaf is part of a subscription
    which has non-trivial arguments, like arithmetic expressions or function calls.
    """
NO: Final[str] = ""
SPACE: Final[str] = " "
DOUBLESPACE: Final[str] = "  "
t = leaf.type
p = leaf.parent
v = leaf.value
if t in ALWAYS_NO_SPACE:
    exit(NO)

if t == token.COMMENT:
    exit(DOUBLESPACE)

assert p is not None, f"INTERNAL ERROR: hand-made leaf without parent: {leaf!r}"
if t == token.COLON and p.type not in {
    syms.subscript,
    syms.subscriptlist,
    syms.sliceop,
}:
    exit(NO)

prev = leaf.prev_sibling
if not prev:
    prevp = preceding_leaf(p)
    if not prevp or prevp.type in OPENING_BRACKETS:
        exit(NO)

    if t == token.COLON:
        if prevp.type == token.COLON:
            exit(NO)

        elif prevp.type != token.COMMA and not complex_subscript:
            exit(NO)

        exit(SPACE)

    if prevp.type == token.EQUAL:
        if prevp.parent:
            if prevp.parent.type in {
                syms.arglist,
                syms.argument,
                syms.parameters,
                syms.varargslist,
            }:
                exit(NO)

            elif prevp.parent.type == syms.typedargslist:
                # A bit hacky: if the equal sign has whitespace, it means we
                # previously found it's a typed argument.  So, we're using
                # that, too.
                exit(prevp.prefix)

    elif (
        prevp.type == token.STAR
        and parent_type(prevp) == syms.star_expr
        and parent_type(prevp.parent) == syms.subscriptlist
    ):
        # No space between typevar tuples.
        exit(NO)

    elif prevp.type in VARARGS_SPECIALS:
        if is_vararg(prevp, within=VARARGS_PARENTS | UNPACKING_PARENTS):
            exit(NO)

    elif prevp.type == token.COLON:
        if prevp.parent and prevp.parent.type in {syms.subscript, syms.sliceop}:
            exit(SPACE if complex_subscript else NO)

    elif (
        prevp.parent
        and prevp.parent.type == syms.factor
        and prevp.type in MATH_OPERATORS
    ):
        exit(NO)

    elif prevp.type == token.AT and p.parent and p.parent.type == syms.decorator:
        # no space in decorators
        exit(NO)

elif prev.type in OPENING_BRACKETS:
    exit(NO)

if p.type in {syms.parameters, syms.arglist}:
    # untyped function signatures or calls
    if not prev or prev.type != token.COMMA:
        exit(NO)

elif p.type == syms.varargslist:
    # lambdas
    if prev and prev.type != token.COMMA:
        exit(NO)

elif p.type == syms.typedargslist:
    # typed function signatures
    if not prev:
        exit(NO)

    if t == token.EQUAL:
        if prev.type not in TYPED_NAMES:
            exit(NO)

    elif prev.type == token.EQUAL:
        # A bit hacky: if the equal sign has whitespace, it means we
        # previously found it's a typed argument.  So, we're using that, too.
        exit(prev.prefix)

    elif prev.type != token.COMMA:
        exit(NO)

elif p.type in TYPED_NAMES:
    # type names
    if not prev:
        prevp = preceding_leaf(p)
        if not prevp or prevp.type != token.COMMA:
            exit(NO)

elif p.type == syms.trailer:
    # attributes and calls
    if t == token.LPAR or t == token.RPAR:
        exit(NO)

    if not prev:
        if t == token.DOT or t == token.LSQB:
            exit(NO)

    elif prev.type != token.COMMA:
        exit(NO)

elif p.type == syms.argument:
    # single argument
    if t == token.EQUAL:
        exit(NO)

    if not prev:
        prevp = preceding_leaf(p)
        if not prevp or prevp.type == token.LPAR:
            exit(NO)

    elif prev.type in {token.EQUAL} | VARARGS_SPECIALS:
        exit(NO)

elif p.type == syms.decorator:
    # decorators
    exit(NO)

elif p.type == syms.dotted_name:
    if prev:
        exit(NO)

    prevp = preceding_leaf(p)
    if not prevp or prevp.type == token.AT or prevp.type == token.DOT:
        exit(NO)

elif p.type == syms.classdef:
    if t == token.LPAR:
        exit(NO)

    if prev and prev.type == token.LPAR:
        exit(NO)

elif p.type in {syms.subscript, syms.sliceop}:
    # indexing
    if not prev:
        assert p.parent is not None, "subscripts are always parented"
        if p.parent.type == syms.subscriptlist:
            exit(SPACE)

        exit(NO)

    elif not complex_subscript:
        exit(NO)

elif p.type == syms.atom:
    if prev and t == token.DOT:
        # dots, but not the first one.
        exit(NO)

elif p.type == syms.dictsetmaker:
    # dict unpacking
    if prev and prev.type == token.DOUBLESTAR:
        exit(NO)

elif p.type in {syms.factor, syms.star_expr}:
    # unary ops
    if not prev:
        prevp = preceding_leaf(p)
        if not prevp or prevp.type in OPENING_BRACKETS:
            exit(NO)

        prevp_parent = prevp.parent
        assert prevp_parent is not None
        if prevp.type == token.COLON and prevp_parent.type in {
            syms.subscript,
            syms.sliceop,
        }:
            exit(NO)

        elif prevp.type == token.EQUAL and prevp_parent.type == syms.argument:
            exit(NO)

    elif t in {token.NAME, token.NUMBER, token.STRING}:
        exit(NO)

elif p.type == syms.import_from:
    if t == token.DOT:
        if prev and prev.type == token.DOT:
            exit(NO)

    elif t == token.NAME:
        if v == "import":
            exit(SPACE)

        if prev and prev.type == token.DOT:
            exit(NO)

elif p.type == syms.sliceop:
    exit(NO)

elif p.type == syms.except_clause:
    if t == token.STAR:
        exit(NO)

exit(SPACE)
