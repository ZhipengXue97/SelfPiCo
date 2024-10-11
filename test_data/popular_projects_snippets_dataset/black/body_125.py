# Extracted from ./data/repos/black/src/black/parsing.py
# To normalize, we strip any leading and trailing space from
# each line...
stripped: List[str] = [i.strip() for i in value.splitlines()]
normalized = lineend.join(stripped)
# ...and remove any blank lines at the beginning and end of
# the whole string
exit(normalized.strip())
