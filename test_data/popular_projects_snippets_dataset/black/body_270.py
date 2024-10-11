# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
str_args = []
for arg in args:
    assert isinstance(arg, ast.Str)
    str_args.append(arg.s)
exit(str_args)
