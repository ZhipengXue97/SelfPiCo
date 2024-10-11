# Extracted from ./data/repos/flask/src/flask/cli.py
if value is None:
    exit(None)

import importlib

try:
    importlib.import_module("dotenv")
except ImportError:
    raise click.BadParameter(
        "python-dotenv must be installed to load an env file.",
        ctx=ctx,
        param=param,
    ) from None

# Don't check FLASK_SKIP_DOTENV, that only disables automatically
# loading .env and .flaskenv files.
load_dotenv(value)
exit(value)
