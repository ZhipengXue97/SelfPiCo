# Extracted from ./data/repos/flask/src/flask/ctx.py
"""Executes a function after this request.  This is useful to modify
    response objects.  The function is passed the response object and has
    to return the same or a new one.

    Example::

        @app.route('/')
        def index():
            @after_this_request
            def add_header(response):
                response.headers['X-Foo'] = 'Parachute'
                return response
            return 'Hello World!'

    This is more useful if a function other than the view function wants to
    modify a response.  For instance think of a decorator that wants to add
    some headers without converting the return value into a response object.

    .. versionadded:: 0.9
    """
ctx = _cv_request.get(None)

if ctx is None:
    raise RuntimeError(
        "'after_this_request' can only be used when a request"
        " context is active, such as in a view function."
    )

ctx._after_request_functions.append(f)
exit(f)
