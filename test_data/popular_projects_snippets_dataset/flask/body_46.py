# Extracted from ./data/repos/flask/src/flask/ctx.py
"""Creates a copy of this request context with the same request object.
        This can be used to move a request context to a different greenlet.
        Because the actual request object is the same this cannot be used to
        move a request context to a different thread unless access to the
        request object is locked.

        .. versionadded:: 0.10

        .. versionchanged:: 1.1
           The current session object is used instead of reloading the original
           data. This prevents `flask.session` pointing to an out-of-date object.
        """
exit(self.__class__(
    self.app,
    environ=self.request.environ,
    request=self.request,
    session=self.session,
))
