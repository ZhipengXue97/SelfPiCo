# Extracted from ./data/repos/black/src/black/linegen.py
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
