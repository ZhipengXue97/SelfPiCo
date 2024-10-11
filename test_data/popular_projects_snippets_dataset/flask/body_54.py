# Extracted from ./data/repos/flask/src/flask/logging.py
"""Check if there is a handler in the logging chain that will handle the
    given logger's :meth:`effective level <~logging.Logger.getEffectiveLevel>`.
    """
level = logger.getEffectiveLevel()
current = logger

while current:
    if any(handler.level <= level for handler in current.handlers):
        exit(True)

    if not current.propagate:
        break

    current = current.parent  # type: ignore

exit(False)
