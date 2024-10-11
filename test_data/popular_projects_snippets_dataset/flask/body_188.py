# Extracted from ./data/repos/flask/src/flask/scaffold.py
"""Open a resource file relative to :attr:`root_path` for
        reading.

        For example, if the file ``schema.sql`` is next to the file
        ``app.py`` where the ``Flask`` app is defined, it can be opened
        with:

        .. code-block:: python

            with app.open_resource("schema.sql") as f:
                conn.executescript(f.read())

        :param resource: Path to the resource relative to
            :attr:`root_path`.
        :param mode: Open the file in this mode. Only reading is
            supported, valid values are "r" (or "rt") and "rb".
        """
if mode not in {"r", "rt", "rb"}:
    raise ValueError("Resources can only be opened for reading.")

exit(open(os.path.join(self.root_path, resource), mode))
