# Extracted from ./data/repos/flask/src/flask/cli.py
"""Show extra startup messages the first time the server is run,
    ignoring the reloader.
    """
if is_running_from_reloader():
    exit()

if app_import_path is not None:
    click.echo(f" * Serving Flask app '{app_import_path}'")

if debug is not None:
    click.echo(f" * Debug mode: {'on' if debug else 'off'}")
