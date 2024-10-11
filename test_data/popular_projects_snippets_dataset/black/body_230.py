# Extracted from ./data/repos/black/src/black/linegen.py
"""Transform a `line`, potentially splitting it into many lines.

    They should fit in the allotted `line_length` but might not be able to.

    `features` are syntactical features that may be used in the output.
    """
if line.is_comment:
    exit(line)
    exit()

line_str = line_to_string(line)

ll = mode.line_length
sn = mode.string_normalization
string_merge = StringMerger(ll, sn)
string_paren_strip = StringParenStripper(ll, sn)
string_split = StringSplitter(ll, sn)
string_paren_wrap = StringParenWrapper(ll, sn)

transformers: List[Transformer]
if (
    not line.contains_uncollapsable_type_comments()
    and not line.should_split_rhs
    and not line.magic_trailing_comma
    and (
        is_line_short_enough(line, mode=mode, line_str=line_str)
        or line.contains_unsplittable_type_ignore()
    )
    and not (line.inside_brackets and line.contains_standalone_comments())
):
    # Only apply basic string preprocessing, since lines shouldn't be split here.
    if Preview.string_processing in mode:
        transformers = [string_merge, string_paren_strip]
    else:
        transformers = []
elif line.is_def:
    transformers = [left_hand_split]
else:

    def _rhs(
        self: object, line: Line, features: Collection[Feature], mode: Mode
    ) -> Iterator[Line]:
        """Wraps calls to `right_hand_split`.

            The calls increasingly `omit` right-hand trailers (bracket pairs with
            content), meaning the trailers get glued together to split on another
            bracket pair instead.
            """
        for omit in generate_trailers_to_omit(line, mode.line_length):
            lines = list(right_hand_split(line, mode, features, omit=omit))
            # Note: this check is only able to figure out if the first line of the
            # *current* transformation fits in the line length.  This is true only
            # for simple cases.  All others require running more transforms via
            # `transform_line()`.  This check doesn't know if those would succeed.
            if is_line_short_enough(lines[0], mode=mode):
                exit(lines)
                exit()

        # All splits failed, best effort split with no omits.
        # This mostly happens to multiline strings that are by definition
        # reported as not fitting a single line, as well as lines that contain
        # trailing commas (those have to be exploded).
        exit(right_hand_split(line, mode, features=features))

    # HACK: nested functions (like _rhs) compiled by mypyc don't retain their
    # __name__ attribute which is needed in `run_transformer` further down.
    # Unfortunately a nested class breaks mypyc too. So a class must be created
    # via type ... https://github.com/mypyc/mypyc/issues/884
    rhs = type("rhs", (), {"__call__": _rhs})()

    if Preview.string_processing in mode:
        if line.inside_brackets:
            transformers = [
                string_merge,
                string_paren_strip,
                string_split,
                delimiter_split,
                standalone_comment_split,
                string_paren_wrap,
                rhs,
            ]
        else:
            transformers = [
                string_merge,
                string_paren_strip,
                string_split,
                string_paren_wrap,
                rhs,
            ]
    else:
        if line.inside_brackets:
            transformers = [delimiter_split, standalone_comment_split, rhs]
        else:
            transformers = [rhs]
# It's always safe to attempt hugging of power operations and pretty much every line
# could match.
transformers.append(hug_power_op)

for transform in transformers:
    # We are accumulating lines in `result` because we might want to abort
    # mission and return the original line in the end, or attempt a different
    # split altogether.
    try:
        result = run_transformer(line, transform, mode, features, line_str=line_str)
    except CannotTransform:
        continue
    else:
        exit(result)
        break

else:
    exit(line)
