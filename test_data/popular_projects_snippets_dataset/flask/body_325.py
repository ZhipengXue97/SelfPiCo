# Extracted from ./data/repos/flask/src/flask/cli.py
"""Given a filename this will try to calculate the python path, add it
    to the search path and return the actual module name that is expected.
    """
path = os.path.realpath(path)

fname, ext = os.path.splitext(path)
if ext == ".py":
    path = fname

if os.path.basename(path) == "__init__":
    path = os.path.dirname(path)

module_name = []

# move up until outside package structure (no __init__.py)
while True:
    path, name = os.path.split(path)
    module_name.append(name)

    if not os.path.exists(os.path.join(path, "__init__.py")):
        break

if sys.path[0] != path:
    sys.path.insert(0, path)

exit(".".join(module_name[::-1]))
