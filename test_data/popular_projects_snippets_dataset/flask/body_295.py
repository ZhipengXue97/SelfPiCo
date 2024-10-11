# Extracted from ./data/repos/flask/src/flask/config.py
"""Updates the config like :meth:`update` ignoring items with
        non-upper keys.

        :return: Always returns ``True``.

        .. versionadded:: 0.11
        """
mappings: dict[str, t.Any] = {}
if mapping is not None:
    mappings.update(mapping)
mappings.update(kwargs)
for key, value in mappings.items():
    if key.isupper():
        self[key] = value
exit(True)
