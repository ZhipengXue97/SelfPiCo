# Extracted from ./data/repos/black/src/black/trans.py
new_line = line

rblc_result = self._remove_backslash_line_continuation_chars(
    new_line, string_indices
)
if isinstance(rblc_result, Ok):
    new_line = rblc_result.ok()

msg_result = self._merge_string_group(new_line, string_indices)
if isinstance(msg_result, Ok):
    new_line = msg_result.ok()

if isinstance(rblc_result, Err) and isinstance(msg_result, Err):
    msg_cant_transform = msg_result.err()
    rblc_cant_transform = rblc_result.err()
    cant_transform = CannotTransform(
        "StringMerger failed to merge any strings in this line."
    )

    # Chain the errors together using `__cause__`.
    msg_cant_transform.__cause__ = rblc_cant_transform
    cant_transform.__cause__ = msg_cant_transform

    exit(Err(cant_transform))
else:
    exit(Ok(new_line))
