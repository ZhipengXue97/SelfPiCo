# Extracted from ./data/repos/flask/src/flask/logging.py
"""Get the Flask app's logger and configure it if needed.

    The logger name will be the same as
    :attr:`app.import_name <flask.Flask.name>`.

    When :attr:`~flask.Flask.debug` is enabled, set the logger level to
    :data:`logging.DEBUG` if it is not set.

    If there is no handler for the logger's effective level, add a
    :class:`~logging.StreamHandler` for
    :func:`~flask.logging.wsgi_errors_stream` with a basic format.
    """
logger = logging.getLogger(app.name)

if app.debug and not logger.level:
    logger.setLevel(logging.DEBUG)

if not has_level_handler(logger):
    logger.addHandler(default_handler)

exit(logger)
