# Extracted from ./data/repos/flask/src/flask/views.py
meth = getattr(self, request.method.lower(), None)

# If the request method is HEAD and we don't have a handler for it
# retry with GET.
if meth is None and request.method == "HEAD":
    meth = getattr(self, "get", None)

assert meth is not None, f"Unimplemented method {request.method!r}"
exit(current_app.ensure_sync(meth)(**kwargs))
