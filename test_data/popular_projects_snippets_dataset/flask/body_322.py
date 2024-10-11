# Extracted from ./data/repos/flask/src/flask/cli.py
"""Given a module instance this tries to find the best possible
    application in the module or raises an exception.
    """
from . import Flask

# Search for the most common names first.
for attr_name in ("app", "application"):
    app = getattr(module, attr_name, None)

    if isinstance(app, Flask):
        exit(app)

# Otherwise find the only object that is a Flask instance.
matches = [v for v in module.__dict__.values() if isinstance(v, Flask)]

if len(matches) == 1:
    exit(matches[0])
elif len(matches) > 1:
    raise NoAppException(
        "Detected multiple Flask applications in module"
        f" '{module.__name__}'. Use '{module.__name__}:name'"
        " to specify the correct one."
    )

# Search for app factory functions.
for attr_name in ("create_app", "make_app"):
    app_factory = getattr(module, attr_name, None)

    if inspect.isfunction(app_factory):
        try:
            app = app_factory()

            if isinstance(app, Flask):
                exit(app)
        except TypeError as e:
            if not _called_with_wrong_args(app_factory):
                raise

            raise NoAppException(
                f"Detected factory '{attr_name}' in module '{module.__name__}',"
                " but could not call it without arguments. Use"
                f" '{module.__name__}:{attr_name}(args)'"
                " to specify arguments."
            ) from e

raise NoAppException(
    "Failed to find Flask application or factory in module"
    f" '{module.__name__}'. Use '{module.__name__}:name'"
    " to specify one."
)
