# Extracted from ./data/repos/flask/src/flask/helpers.py
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
