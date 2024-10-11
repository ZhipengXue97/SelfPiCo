# Extracted from ./data/repos/flask/src/flask/app.py
"""Called right before the application context is popped.

        When handling a request, the application context is popped
        after the request context. See :meth:`do_teardown_request`.

        This calls all functions decorated with
        :meth:`teardown_appcontext`. Then the
        :data:`appcontext_tearing_down` signal is sent.

        This is called by
        :meth:`AppContext.pop() <flask.ctx.AppContext.pop>`.

        .. versionadded:: 0.9
        """
if exc is _sentinel:
    exc = sys.exc_info()[1]

for func in reversed(self.teardown_appcontext_funcs):
    self.ensure_sync(func)(exc)

appcontext_tearing_down.send(self, _async_wrapper=self.ensure_sync, exc=exc)
