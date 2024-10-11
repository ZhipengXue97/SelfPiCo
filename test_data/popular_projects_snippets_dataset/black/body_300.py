# Extracted from ./data/repos/black/src/black/__init__.py
"""Format code in given cell of Jupyter notebook.

    General idea is:

      - if cell has trailing semicolon, remove it;
      - if cell has IPython magics, mask them;
      - format cell;
      - reinstate IPython magics;
      - reinstate trailing semicolon (if originally present);
      - strip trailing newlines.

    Cells with syntax errors will not be processed, as they
    could potentially be automagics or multi-line magics, which
    are currently not supported.
    """
validate_cell(src, mode)
src_without_trailing_semicolon, has_trailing_semicolon = remove_trailing_semicolon(
    src
)
try:
    masked_src, replacements = mask_cell(src_without_trailing_semicolon)
except SyntaxError:
    raise NothingChanged from None
masked_dst = format_str(masked_src, mode=mode)
if not fast:
    check_stability_and_equivalence(masked_src, masked_dst, mode=mode)
dst_without_trailing_semicolon = unmask_cell(masked_dst, replacements)
dst = put_trailing_semicolon_back(
    dst_without_trailing_semicolon, has_trailing_semicolon
)
dst = dst.rstrip("\n")
if dst == src:
    raise NothingChanged from None
exit(dst)
