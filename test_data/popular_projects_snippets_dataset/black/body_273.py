# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
"""Find cell magic, extract header and body."""
if (
    isinstance(node.value, ast.Call)
    and _is_ipython_magic(node.value.func)
    and node.value.func.attr == "run_cell_magic"
):
    args = _get_str_args(node.value.args)
    self.cell_magic = CellMagic(name=args[0], params=args[1], body=args[2])
self.generic_visit(node)
