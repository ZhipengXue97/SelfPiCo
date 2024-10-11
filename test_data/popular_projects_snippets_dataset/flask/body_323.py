# Extracted from ./data/repos/flask/src/flask/cli.py
"""Check whether calling a function raised a ``TypeError`` because
    the call failed or because something in the factory raised the
    error.

    :param f: The function that was called.
    :return: ``True`` if the call failed.
    """
tb = sys.exc_info()[2]

try:
    while tb is not None:
        if tb.tb_frame.f_code is f.__code__:
            # In the function, it was called successfully.
            exit(False)

        tb = tb.tb_next

    # Didn't reach the function.
    exit(True)
finally:
    # Delete tb to break a circular reference.
    # https://docs.python.org/2/library/sys.html#sys.exc_info
    del tb
