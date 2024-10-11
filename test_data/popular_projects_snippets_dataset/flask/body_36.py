# Extracted from ./data/repos/flask/src/flask/ctx.py
with ctx:
    exit(ctx.app.ensure_sync(f)(*args, **kwargs))
