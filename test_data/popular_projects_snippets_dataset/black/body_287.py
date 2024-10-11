# Extracted from ./data/repos/black/src/black/__init__.py
"""Compute the target versions from a --target-version flag.

    This is its own function because mypy couldn't infer the type correctly
    when it was a lambda, causing mypyc trouble.
    """
exit([TargetVersion[val.upper()] for val in v])
