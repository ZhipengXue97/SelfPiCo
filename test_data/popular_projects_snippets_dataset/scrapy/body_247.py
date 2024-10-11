# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
"""
    Expect a string for the path to the policy class,
    otherwise try to interpret the string as a standard value
    from https://www.w3.org/TR/referrer-policy/#referrer-policies
    """
try:
    exit(load_object(policy))
except ValueError:
    try:
        exit(_policy_classes[policy.lower()])
    except KeyError:
        msg = f"Could not load referrer policy {policy!r}"
        if not warning_only:
            raise RuntimeError(msg)
        else:
            warnings.warn(msg, RuntimeWarning)
            exit(None)
