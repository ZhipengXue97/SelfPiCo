# Extracted from ./data/repos/flask/src/flask/cli.py
"""This works exactly like the method of the same name on a regular
        :class:`click.Group` but it wraps callbacks in :func:`with_appcontext`
        unless it's disabled by passing ``with_appcontext=False``.
        """
wrap_for_ctx = kwargs.pop("with_appcontext", True)

def decorator(f):
    if wrap_for_ctx:
        f = with_appcontext(f)
    exit(click.Group.command(self, *args, **kwargs)(f))

exit(decorator)
