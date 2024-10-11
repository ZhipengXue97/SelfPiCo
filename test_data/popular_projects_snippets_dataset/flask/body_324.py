# Extracted from ./data/repos/flask/src/flask/cli.py
"""Check if the given string is a variable name or a function. Call
    a function to get the app instance, or return the variable directly.
    """
from . import Flask

# Parse app_name as a single expression to determine if it's a valid
# attribute name or function call.
try:
    expr = ast.parse(app_name.strip(), mode="eval").body
except SyntaxError:
    raise NoAppException(
        f"Failed to parse {app_name!r} as an attribute name or function call."
    ) from None

if isinstance(expr, ast.Name):
    name = expr.id
    args = []
    kwargs = {}
elif isinstance(expr, ast.Call):
    # Ensure the function name is an attribute name only.
    if not isinstance(expr.func, ast.Name):
        raise NoAppException(
            f"Function reference must be a simple name: {app_name!r}."
        )

    name = expr.func.id

    # Parse the positional and keyword arguments as literals.
    try:
        args = [ast.literal_eval(arg) for arg in expr.args]
        kwargs = {kw.arg: ast.literal_eval(kw.value) for kw in expr.keywords}
    except ValueError:
        # literal_eval gives cryptic error messages, show a generic
        # message with the full expression instead.
        raise NoAppException(
            f"Failed to parse arguments as literal values: {app_name!r}."
        ) from None
else:
    raise NoAppException(
        f"Failed to parse {app_name!r} as an attribute name or function call."
    )

try:
    attr = getattr(module, name)
except AttributeError as e:
    raise NoAppException(
        f"Failed to find attribute {name!r} in {module.__name__!r}."
    ) from e

# If the attribute is a function, call it with any args and kwargs
# to get the real application.
if inspect.isfunction(attr):
    try:
        app = attr(*args, **kwargs)
    except TypeError as e:
        if not _called_with_wrong_args(attr):
            raise

        raise NoAppException(
            f"The factory {app_name!r} in module"
            f" {module.__name__!r} could not be called with the"
            " specified arguments."
        ) from e
else:
    app = attr

if isinstance(app, Flask):
    exit(app)

raise NoAppException(
    "A valid Flask application was not obtained from"
    f" '{module.__name__}:{app_name}'."
)
