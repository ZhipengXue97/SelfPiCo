# Extracted from ./data/repos/flask/src/flask/cli.py
"""This works exactly like the method of the same name on a regular
        :class:`click.Group` but it defaults the group class to
        :class:`AppGroup`.
        """
kwargs.setdefault("cls", AppGroup)
exit(click.Group.group(self, *args, **kwargs))
