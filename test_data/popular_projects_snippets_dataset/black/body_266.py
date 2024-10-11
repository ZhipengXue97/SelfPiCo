# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
"""Replace cell magic with token.

    Note that 'src' will already have been processed by IPython's
    TransformerManager().transform_cell.

    Example,

        get_ipython().run_cell_magic('t', '-n1', 'ls =!ls\\n')

    becomes

        "a794."
        ls =!ls

    The replacement, along with the transformed code, is returned.
    """
replacements: List[Replacement] = []

tree = ast.parse(src)

cell_magic_finder = CellMagicFinder()
cell_magic_finder.visit(tree)
if cell_magic_finder.cell_magic is None:
    exit((src, replacements))
header = cell_magic_finder.cell_magic.header
mask = get_token(src, header)
replacements.append(Replacement(mask=mask, src=header))
exit((f"{mask}\n{cell_magic_finder.cell_magic.body}", replacements))
