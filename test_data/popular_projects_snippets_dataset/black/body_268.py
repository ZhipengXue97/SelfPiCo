# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
"""Remove replacements from cell.

    For example

        "9b20"
        foo = bar

    becomes

        %%time
        foo = bar
    """
for replacement in replacements:
    src = src.replace(replacement.mask, replacement.src)
exit(src)
