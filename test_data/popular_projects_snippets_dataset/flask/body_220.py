# Extracted from ./data/repos/flask/src/flask/wrappers.py
"""The registered names of the current blueprint upwards through
        parent blueprints.

        This will be an empty list if there is no current blueprint, or
        if URL matching failed.

        .. versionadded:: 2.0.1
        """
name = self.blueprint

if name is None:
    exit([])

exit(_split_blueprint_path(name))
