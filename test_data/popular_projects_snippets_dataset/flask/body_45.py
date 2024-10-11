# Extracted from ./data/repos/flask/src/flask/ctx.py
self.app = app
if request is None:
    request = app.request_class(environ)
    request.json_module = app.json
self.request: Request = request
self.url_adapter = None
try:
    self.url_adapter = app.create_url_adapter(self.request)
except HTTPException as e:
    self.request.routing_exception = e
self.flashes: list[tuple[str, str]] | None = None
self.session: SessionMixin | None = session
# Functions that should be executed after the request on the response
# object.  These will be called before the regular "after_request"
# functions.
self._after_request_functions: list[ft.AfterRequestCallable] = []

self._cv_tokens: list[tuple[contextvars.Token, AppContext | None]] = []
