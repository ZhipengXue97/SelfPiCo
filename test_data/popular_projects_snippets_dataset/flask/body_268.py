# Extracted from ./data/repos/flask/src/flask/helpers.py
"""Request contexts disappear when the response is started on the server.
    This is done for efficiency reasons and to make it less likely to encounter
    memory leaks with badly written WSGI middlewares.  The downside is that if
    you are using streamed responses, the generator cannot access request bound
    information any more.

    This function however can help you keep the context around for longer::

        from flask import stream_with_context, request, Response

        @app.route('/stream')
        def streamed_response():
            @stream_with_context
            def generate():
                yield 'Hello '
                yield request.args['name']
                yield '!'
            return Response(generate())

    Alternatively it can also be used around a specific generator::

        from flask import stream_with_context, request, Response

        @app.route('/stream')
        def streamed_response():
            def generate():
                yield 'Hello '
                yield request.args['name']
                yield '!'
            return Response(stream_with_context(generate()))

    .. versionadded:: 0.9
    """
try:
    gen = iter(generator_or_function)  # type: ignore
except TypeError:

    def decorator(*args: t.Any, **kwargs: t.Any) -> t.Any:
        gen = generator_or_function(*args, **kwargs)  # type: ignore
        exit(stream_with_context(gen))

    exit(update_wrapper(decorator, generator_or_function))  # type: ignore

def generator() -> t.Generator:
    ctx = _cv_request.get(None)
    if ctx is None:
        raise RuntimeError(
            "'stream_with_context' can only be used when a request"
            " context is active, such as in a view function."
        )
    with ctx:
        # Dummy sentinel.  Has to be inside the context block or we're
        # not actually keeping the context around.
        exit(None)

        # The try/finally is here so that if someone passes a WSGI level
        # iterator in we're still running the cleanup logic.  Generators
        # don't need that because they are closed on their destruction
        # automatically.
        try:
            exit(gen)
        finally:
            if hasattr(gen, "close"):
                gen.close()

# The trick is to start the generator.  Then the code execution runs until
# the first dummy None is yielded at which point the context was already
# pushed.  This item is discarded.  Then when the iteration continues the
# real generator is executed.
wrapped_g = generator()
next(wrapped_g)
exit(wrapped_g)
