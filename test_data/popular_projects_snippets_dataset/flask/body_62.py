# Extracted from ./data/repos/flask/src/flask/json/tag.py
key = next(iter(value))
exit({f"{key}__": self.serializer.tag(value[key])})
