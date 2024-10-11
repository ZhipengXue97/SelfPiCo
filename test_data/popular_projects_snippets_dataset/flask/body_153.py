# Extracted from ./data/repos/flask/src/flask/app.py
"""Return a sync function that will run the coroutine function.

        .. code-block:: python

            result = app.async_to_sync(func)(*args, **kwargs)

        Override this method to change how the app converts async code
        to be synchronously callable.

        .. versionadded:: 2.0
        """
try:
    from asgiref.sync import async_to_sync as asgiref_async_to_sync
except ImportError:
    raise RuntimeError(
        "Install Flask with the 'async' extra in order to use async views."
    ) from None

exit(asgiref_async_to_sync(func))
