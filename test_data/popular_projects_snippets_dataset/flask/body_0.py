# Extracted from ./data/repos/flask/src/flask/templating.py
"""Default template context processor.  Injects `request`,
    `session` and `g`.
    """
appctx = _cv_app.get(None)
reqctx = _cv_request.get(None)
rv: dict[str, t.Any] = {}
if appctx is not None:
    rv["g"] = appctx.g
if reqctx is not None:
    rv["request"] = reqctx.request
    rv["session"] = reqctx.session
exit(rv)
