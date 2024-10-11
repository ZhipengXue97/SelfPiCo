# Extracted from ./data/repos/flask/src/flask/cli.py
if wrap_for_ctx:
    f = with_appcontext(f)
exit(click.Group.command(self, *args, **kwargs)(f))
