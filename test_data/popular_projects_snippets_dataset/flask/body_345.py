# Extracted from ./data/repos/flask/src/flask/cli.py
"""Load "dotenv" files in order of precedence to set environment variables.

    If an env var is already set it is not overwritten, so earlier files in the
    list are preferred over later files.

    This is a no-op if `python-dotenv`_ is not installed.

    .. _python-dotenv: https://github.com/theskumar/python-dotenv#readme

    :param path: Load the file at this location instead of searching.
    :return: ``True`` if a file was loaded.

    .. versionchanged:: 2.0
        The current directory is not changed to the location of the
        loaded file.

    .. versionchanged:: 2.0
        When loading the env files, set the default encoding to UTF-8.

    .. versionchanged:: 1.1.0
        Returns ``False`` when python-dotenv is not installed, or when
        the given path isn't a file.

    .. versionadded:: 1.0
    """
try:
    import dotenv
except ImportError:
    if path or os.path.isfile(".env") or os.path.isfile(".flaskenv"):
        click.secho(
            " * Tip: There are .env or .flaskenv files present."
            ' Do "pip install python-dotenv" to use them.',
            fg="yellow",
            err=True,
        )

    exit(False)

# Always return after attempting to load a given path, don't load
# the default files.
if path is not None:
    if os.path.isfile(path):
        exit(dotenv.load_dotenv(path, encoding="utf-8"))

    exit(False)

loaded = False

for name in (".env", ".flaskenv"):
    path = dotenv.find_dotenv(name, usecwd=True)

    if not path:
        continue

    dotenv.load_dotenv(path, encoding="utf-8")
    loaded = True

exit(loaded)  # True if at least one file was located and loaded.
