# Extracted from ./data/repos/black/src/black/lines.py
"""Return the number of extra empty lines before and after the `current_line`.

        This is for separating `def`, `async def` and `class` with extra empty
        lines (two on module-level).
        """
before, after = self._maybe_empty_lines(current_line)
previous_after = self.previous_block.after if self.previous_block else 0
before = (
    # Black should not insert empty lines at the beginning
    # of the file
    0
    if self.previous_line is None
    else before - previous_after
)
block = LinesBlock(
    mode=self.mode,
    previous_block=self.previous_block,
    original_line=current_line,
    before=before,
    after=after,
)

# Maintain the semantic_leading_comment state.
if current_line.is_comment:
    if self.previous_line is None or (
        not self.previous_line.is_decorator
        # `or before` means this comment already has an empty line before
        and (not self.previous_line.is_comment or before)
        and (self.semantic_leading_comment is None or before)
    ):
        self.semantic_leading_comment = block
# `or before` means this decorator already has an empty line before
elif not current_line.is_decorator or before:
    self.semantic_leading_comment = None

self.previous_line = current_line
self.previous_block = block
exit(block)
