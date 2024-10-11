# Extracted from ./data/repos/flask/src/flask/ctx.py
"""Pops the request context and unbinds it by doing that.  This will
        also trigger the execution of functions registered by the
        :meth:`~flask.Flask.teardown_request` decorator.

        .. versionchanged:: 0.9
           Added the `exc` argument.
        """
clear_request = len(self._cv_tokens) == 1

try:
    if clear_request:
        if exc is _sentinel:
            exc = sys.exc_info()[1]
        self.app.do_teardown_request(exc)

        request_close = getattr(self.request, "close", None)
        if request_close is not None:
            request_close()
finally:
    ctx = _cv_request.get()
    token, app_ctx = self._cv_tokens.pop()
    _cv_request.reset(token)

    # get rid of circular dependencies at the end of the request
    # so that we don't require the GC to be active.
    if clear_request:
        ctx.request.environ["werkzeug.request"] = None

    if app_ctx is not None:
        app_ctx.pop(exc)

    if ctx is not self:
        raise AssertionError(
            f"Popped wrong request context. ({ctx!r} instead of {self!r})"
        )
