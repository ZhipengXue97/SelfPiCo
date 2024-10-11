# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
"""Returns a unique key to use for caching.

    Subclasses must override this.

    Calls made to `transform_function` with functions that have the same code
    object and caching key will return a cached instance on subsequent
    invocations.

    Args:
      user_context: The context object which was passed to `transform`.

    Returns:
      extra_locals: A hashable.
    """
raise NotImplementedError('subclasses must override this')
