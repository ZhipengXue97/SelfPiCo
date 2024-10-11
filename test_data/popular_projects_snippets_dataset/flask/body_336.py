# Extracted from ./data/repos/flask/src/flask/cli.py
# If the flag isn't provided, it will default to False. Don't use
# that, let debug be set by env in that case.
source = ctx.get_parameter_source(param.name)  # type: ignore[arg-type]

if source is not None and source in (
    ParameterSource.DEFAULT,
    ParameterSource.DEFAULT_MAP,
):
    exit(None)

# Set with env var instead of ScriptInfo.load so that it can be
# accessed early during a factory function.
os.environ["FLASK_DEBUG"] = "1" if value else "0"
exit(value)
