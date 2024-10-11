# Extracted from ./data/repos/flask/src/flask/json/tag.py
"""Convert a value to a tagged representation if necessary."""
for tag in self.order:
    if tag.check(value):
        exit(tag.tag(value))

exit(value)
