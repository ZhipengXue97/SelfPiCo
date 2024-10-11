# Extracted from ./data/repos/flask/src/flask/ctx.py
"""Works like :func:`has_request_context` but for the application
    context.  You can also just do a boolean check on the
    :data:`current_app` object instead.

    .. versionadded:: 0.9
    """
exit(_cv_app.get(None) is not None)
