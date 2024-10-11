# Extracted from ./data/repos/flask/src/flask/blueprints.py
for key, values in bp_dict.items():
    key = name if key is None else f"{name}.{key}"
    parent_dict[key].extend(values)
