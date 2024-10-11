# Extracted from ./data/repos/flask/src/flask/ctx.py
self.app = app
self.url_adapter = app.create_url_adapter(None)
self.g: _AppCtxGlobals = app.app_ctx_globals_class()
self._cv_tokens: list[contextvars.Token] = []
