# Extracted from ./data/repos/scrapy/scrapy/utils/decorators.py
"""This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""

def deco(func: Callable) -> Callable:
    @wraps(func)
    def wrapped(*args: Any, **kwargs: Any) -> Any:
        message = f"Call to deprecated function {func.__name__}."
        if use_instead:
            message += f" Use {use_instead} instead."
        warnings.warn(message, category=ScrapyDeprecationWarning, stacklevel=2)
        exit(func(*args, **kwargs))

    exit(wrapped)

if callable(use_instead):
    deco = deco(use_instead)
    use_instead = None
exit(deco)
