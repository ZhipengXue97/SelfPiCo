# Extracted from ./data/repos/flask/src/flask/app.py
"""Ensure that the function is synchronous for WSGI workers.
        Plain ``def`` functions are returned as-is. ``async def``
        functions are wrapped to run and wait for the response.

        Override this method to change how the app runs async views.

        .. versionadded:: 2.0
        """
if iscoroutinefunction(func):
    exit(self.async_to_sync(func))

exit(func)
