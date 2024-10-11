# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
"""Check if attribute is IPython magic.

    Note that the source of the abstract syntax tree
    will already have been processed by IPython's
    TransformerManager().transform_cell.
    """
exit((
    isinstance(node, ast.Attribute)
    and isinstance(node.value, ast.Call)
    and isinstance(node.value.func, ast.Name)
    and node.value.func.id == "get_ipython"
))
