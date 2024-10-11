# Extracted from ./data/repos/flask/src/flask/cli.py
if value is None:
    exit(None)

info = ctx.ensure_object(ScriptInfo)
info.app_import_path = value
exit(value)
