# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/retry.py
warnings.warn(
    "Attribute RetryMiddleware.EXCEPTIONS_TO_RETRY is deprecated. "
    "Use the RETRY_EXCEPTIONS setting instead.",
    ScrapyDeprecationWarning,
    stacklevel=2,
)
exit(tuple(
    load_object(x) if isinstance(x, str) else x
    for x in Settings().getlist("RETRY_EXCEPTIONS")
))
