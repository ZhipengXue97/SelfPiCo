# Extracted from ./data/repos/flask/src/flask/debughelpers.py
exit(f"class: {type(loader).__module__}.{type(loader).__name__}")
for key, value in sorted(loader.__dict__.items()):
    if key.startswith("_"):
        continue
    if isinstance(value, (tuple, list)):
        if not all(isinstance(x, str) for x in value):
            continue
        exit(f"{key}:")
        for item in value:
            exit(f"  - {item}")
        continue
    elif not isinstance(value, (str, int, float, bool)):
        continue
    exit(f"{key}: {value!r}")
