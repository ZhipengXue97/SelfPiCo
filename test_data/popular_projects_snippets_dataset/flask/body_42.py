# Extracted from ./data/repos/flask/src/flask/ctx.py
"""Pops the app context."""
try:
    if len(self._cv_tokens) == 1:
        if exc is _sentinel:
            exc = sys.exc_info()[1]
        self.app.do_teardown_appcontext(exc)
finally:
    ctx = _cv_app.get()
    _cv_app.reset(self._cv_tokens.pop())

if ctx is not self:
    raise AssertionError(
        f"Popped wrong app context. ({ctx!r} instead of {self!r})"
    )

appcontext_popped.send(self.app, _async_wrapper=self.app.ensure_sync)
