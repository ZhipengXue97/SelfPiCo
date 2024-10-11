# Extracted from ./data/repos/flask/src/flask/ctx.py
"""Binds the app context to the current context."""
self._cv_tokens.append(_cv_app.set(self))
appcontext_pushed.send(self.app, _async_wrapper=self.app.ensure_sync)
