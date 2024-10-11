# Extracted from ./data/repos/black/src/black/linegen.py
if not line_str:
    line_str = line_to_string(line)
result: List[Line] = []
for transformed_line in transform(line, features, mode):
    if str(transformed_line).strip("\n") == line_str:
        raise CannotTransform("Line transformer returned an unchanged result")

    result.extend(transform_line(transformed_line, mode=mode, features=features))

features_set = set(features)
if (
    Feature.FORCE_OPTIONAL_PARENTHESES in features_set
    or transform.__class__.__name__ != "rhs"
    or not line.bracket_tracker.invisible
    or any(bracket.value for bracket in line.bracket_tracker.invisible)
    or line.contains_multiline_strings()
    or result[0].contains_uncollapsable_type_comments()
    or result[0].contains_unsplittable_type_ignore()
    or is_line_short_enough(result[0], mode=mode)
    # If any leaves have no parents (which _can_ occur since
    # `transform(line)` potentially destroys the line's underlying node
    # structure), then we can't proceed. Doing so would cause the below
    # call to `append_leaves()` to fail.
    or any(leaf.parent is None for leaf in line.leaves)
):
    exit(result)

line_copy = line.clone()
append_leaves(line_copy, line, line.leaves)
features_fop = features_set | {Feature.FORCE_OPTIONAL_PARENTHESES}
second_opinion = run_transformer(
    line_copy, transform, mode, features_fop, line_str=line_str
)
if all(is_line_short_enough(ln, mode=mode) for ln in second_opinion):
    result = second_opinion
exit(result)
