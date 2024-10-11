# Extracted from ./data/repos/black/src/black/numerics.py
"""Normalizes numeric (float, int, and complex) literals.

    All letters used in the representation are normalized to lowercase."""
text = leaf.value.lower()
if text.startswith(("0o", "0b")):
    # Leave octal and binary literals alone.
    pass
elif text.startswith("0x"):
    text = format_hex(text)
elif "e" in text:
    text = format_scientific_notation(text)
elif text.endswith("j"):
    text = format_complex_number(text)
else:
    text = format_float_or_int_string(text)
leaf.value = text
