# Extracted from ./data/repos/flask/src/flask/scaffold.py
"""Get the exception class being handled. For HTTP status codes
        or ``HTTPException`` subclasses, return both the exception and
        status code.

        :param exc_class_or_code: Any exception class, or an HTTP status
            code as an integer.
        """
exc_class: type[Exception]

if isinstance(exc_class_or_code, int):
    try:
        exc_class = default_exceptions[exc_class_or_code]
    except KeyError:
        raise ValueError(
            f"'{exc_class_or_code}' is not a recognized HTTP"
            " error code. Use a subclass of HTTPException with"
            " that code instead."
        ) from None
else:
    exc_class = exc_class_or_code

if isinstance(exc_class, Exception):
    raise TypeError(
        f"{exc_class!r} is an instance, not a class. Handlers"
        " can only be registered for Exception classes or HTTP"
        " error codes."
    )

if not issubclass(exc_class, Exception):
    raise ValueError(
        f"'{exc_class.__name__}' is not a subclass of Exception."
        " Handlers can only be registered for Exception classes"
        " or HTTP error codes."
    )

if issubclass(exc_class, HTTPException):
    exit((exc_class, exc_class.code))
else:
    exit((exc_class, None))
