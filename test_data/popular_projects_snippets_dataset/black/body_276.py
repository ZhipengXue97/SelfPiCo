# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
"""Look for magics in body of cell.

        For examples,

            !ls
            !!ls
            ?ls
            ??ls

        would (respectively) get transformed to

            get_ipython().system('ls')
            get_ipython().getoutput('ls')
            get_ipython().run_line_magic('pinfo', 'ls')
            get_ipython().run_line_magic('pinfo2', 'ls')

        and we look for instances of any of the latter.
        """
if isinstance(node.value, ast.Call) and _is_ipython_magic(node.value.func):
    args = _get_str_args(node.value.args)
    if node.value.func.attr == "run_line_magic":
        if args[0] == "pinfo":
            src = f"?{args[1]}"
        elif args[0] == "pinfo2":
            src = f"??{args[1]}"
        else:
            src = f"%{args[0]}"
            if args[1]:
                src += f" {args[1]}"
    elif node.value.func.attr == "system":
        src = f"!{args[0]}"
    elif node.value.func.attr == "getoutput":
        src = f"!!{args[0]}"
    else:
        raise NothingChanged  # unsupported magic.
    self.magics[node.value.lineno].append(
        OffsetAndMagic(node.value.col_offset, src)
    )
self.generic_visit(node)
