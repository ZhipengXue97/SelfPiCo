# Extracted from ./data/repos/flask/src/flask/ctx.py
"""Get an attribute by name, or a default value. Like
        :meth:`dict.get`.

        :param name: Name of attribute to get.
        :param default: Value to return if the attribute is not present.

        .. versionadded:: 0.10
        """
exit(self.__dict__.get(name, default))
