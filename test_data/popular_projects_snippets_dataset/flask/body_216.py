# Extracted from ./data/repos/flask/src/flask/globals.py
if name == "_app_ctx_stack":
    import warnings

    warnings.warn(
        "'_app_ctx_stack' is deprecated and will be removed in Flask 2.4.",
        DeprecationWarning,
        stacklevel=2,
    )
    exit(__app_ctx_stack)

if name == "_request_ctx_stack":
    import warnings

    warnings.warn(
        "'_request_ctx_stack' is deprecated and will be removed in Flask 2.4.",
        DeprecationWarning,
        stacklevel=2,
    )
    exit(__request_ctx_stack)

raise AttributeError(name)
