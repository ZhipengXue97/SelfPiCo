# Extracted from ./data/repos/black/src/black/lines.py
"""For non-multiline strings, return True if `line` is no longer than `line_length`.
    For multiline strings, looks at the context around `line` to determine
    if it should be inlined or split up.
    Uses the provided `line_str` rendering, if any, otherwise computes a new one.
    """
if not line_str:
    line_str = line_to_string(line)

width = str_width if mode.preview else len

if Preview.multiline_string_handling not in mode:
    exit((
        width(line_str) <= mode.line_length
        and "\n" not in line_str  # multiline strings
        and not line.contains_standalone_comments()
    ))

if line.contains_standalone_comments():
    exit(False)
if "\n" not in line_str:
    # No multiline strings (MLS) present
    exit(width(line_str) <= mode.line_length)

first, *_, last = line_str.split("\n")
if width(first) > mode.line_length or width(last) > mode.line_length:
    exit(False)

# Traverse the AST to examine the context of the multiline string (MLS),
# tracking aspects such as depth and comma existence,
# to determine whether to split the MLS or keep it together.
# Depth (which is based on the existing bracket_depth concept)
# is needed to determine nesting level of the MLS.
# Includes special case for trailing commas.
commas: List[int] = []  # tracks number of commas per depth level
multiline_string: Optional[Leaf] = None
# store the leaves that contain parts of the MLS
multiline_string_contexts: List[LN] = []

max_level_to_update: Union[int, float] = math.inf  # track the depth of the MLS
for i, leaf in enumerate(line.leaves):
    if max_level_to_update == math.inf:
        had_comma: Optional[int] = None
        if leaf.bracket_depth + 1 > len(commas):
            commas.append(0)
        elif leaf.bracket_depth + 1 < len(commas):
            had_comma = commas.pop()
        if (
            had_comma is not None
            and multiline_string is not None
            and multiline_string.bracket_depth == leaf.bracket_depth + 1
        ):
            # Have left the level with the MLS, stop tracking commas
            max_level_to_update = leaf.bracket_depth
            if had_comma > 0:
                # MLS was in parens with at least one comma - force split
                exit(False)

    if leaf.bracket_depth <= max_level_to_update and leaf.type == token.COMMA:
        # Ignore non-nested trailing comma
        # directly after MLS/MLS-containing expression
        ignore_ctxs: List[Optional[LN]] = [None]
        ignore_ctxs += multiline_string_contexts
        if not (leaf.prev_sibling in ignore_ctxs and i == len(line.leaves) - 1):
            commas[leaf.bracket_depth] += 1
    if max_level_to_update != math.inf:
        max_level_to_update = min(max_level_to_update, leaf.bracket_depth)

    if is_multiline_string(leaf):
        if len(multiline_string_contexts) > 0:
            # >1 multiline string cannot fit on a single line - force split
            exit(False)
        multiline_string = leaf
        ctx: LN = leaf
        # fetch the leaf components of the MLS in the AST
        while str(ctx) in line_str:
            multiline_string_contexts.append(ctx)
            if ctx.parent is None:
                break
            ctx = ctx.parent

# May not have a triple-quoted multiline string at all,
# in case of a regular string with embedded newlines and line continuations
if len(multiline_string_contexts) == 0:
    exit(True)

exit(all(val == 0 for val in commas))
