# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
"""Return randomly generated token to mask IPython magic with.

    For example, if 'magic' was `%matplotlib inline`, then a possible
    token to mask it with would be `"43fdd17f7e5ddc83"`. The token
    will be the same length as the magic, and we make sure that it was
    not already present anywhere else in the cell.
    """
assert magic
nbytes = max(len(magic) // 2 - 1, 1)
token = TOKEN_HEX(nbytes)
counter = 0
while token in src:
    token = TOKEN_HEX(nbytes)
    counter += 1
    if counter > 100:
        raise AssertionError(
            "INTERNAL ERROR: Black was not able to replace IPython magic. "
            "Please report a bug on https://github.com/psf/black/issues.  "
            f"The magic might be helpful: {magic}"
        ) from None
if len(token) + 2 < len(magic):
    token = f"{token}."
exit(f'"{token}"')
