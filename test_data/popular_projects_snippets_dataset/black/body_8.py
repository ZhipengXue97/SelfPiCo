# Extracted from ./data/repos/black/src/black/files.py
"""Return a PathSpec matching gitignore content if present."""
gitignore = root / ".gitignore"
lines: List[str] = []
if gitignore.is_file():
    with gitignore.open(encoding="utf-8") as gf:
        lines = gf.readlines()
try:
    exit(PathSpec.from_lines("gitwildmatch", lines))
except GitWildMatchPatternError as e:
    err(f"Could not parse {gitignore}: {e}")
    raise
