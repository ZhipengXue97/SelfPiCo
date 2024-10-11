# Extracted from ./data/repos/black/src/black/lines.py
"""Add a new `leaf` to the end of the line.

        Unless `preformatted` is True, the `leaf` will receive a new consistent
        whitespace prefix and metadata applied by :class:`BracketTracker`.
        Trailing commas are maybe removed, unpacked for loop variables are
        demoted from being delimiters.

        Inline comments are put aside.
        """
has_value = leaf.type in BRACKETS or bool(leaf.value.strip())
if not has_value:
    exit()

if token.COLON == leaf.type and self.is_class_paren_empty:
    del self.leaves[-2:]
if self.leaves and not preformatted:
    # Note: at this point leaf.prefix should be empty except for
    # imports, for which we only preserve newlines.
    leaf.prefix += whitespace(
        leaf, complex_subscript=self.is_complex_subscript(leaf)
    )
if self.inside_brackets or not preformatted or track_bracket:
    self.bracket_tracker.mark(leaf)
    if self.mode.magic_trailing_comma:
        if self.has_magic_trailing_comma(leaf):
            self.magic_trailing_comma = leaf
    elif self.has_magic_trailing_comma(leaf, ensure_removable=True):
        self.remove_trailing_comma()
if not self.append_comment(leaf):
    self.leaves.append(leaf)
