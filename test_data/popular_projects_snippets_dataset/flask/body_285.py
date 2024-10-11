# Extracted from ./data/repos/flask/src/flask/helpers.py
out: list[str] = [name]

if "." in name:
    out.extend(_split_blueprint_path(name.rpartition(".")[0]))

exit(out)
