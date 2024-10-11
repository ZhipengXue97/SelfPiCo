# Extracted from ./data/repos/flask/src/flask/cli.py
if not current_app:
    app = __ctx.ensure_object(ScriptInfo).load_app()
    __ctx.with_resource(app.app_context())

exit(__ctx.invoke(f, *args, **kwargs))
