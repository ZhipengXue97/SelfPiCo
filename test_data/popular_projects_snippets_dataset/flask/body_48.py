# Extracted from ./data/repos/flask/src/flask/ctx.py
# Before we push the request context we have to ensure that there
# is an application context.
app_ctx = _cv_app.get(None)

if app_ctx is None or app_ctx.app is not self.app:
    app_ctx = self.app.app_context()
    app_ctx.push()
else:
    app_ctx = None

self._cv_tokens.append((_cv_request.set(self), app_ctx))

# Open the session at the moment that the request context is available.
# This allows a custom open_session method to use the request context.
# Only open a new session if this is the first time the request was
# pushed, otherwise stream_with_context loses the session.
if self.session is None:
    session_interface = self.app.session_interface
    self.session = session_interface.open_session(self.app, self.request)

    if self.session is None:
        self.session = session_interface.make_null_session(self.app)

# Match the request URL after loading the session, so that the
# session is available in custom URL converters.
if self.url_adapter is not None:
    self.match_request()
