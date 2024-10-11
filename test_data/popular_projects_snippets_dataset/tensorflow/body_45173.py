# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_optimizer.py
"""Return a slot named "name" created for "var" by the Optimizer.

    This simply wraps the get_slot() from the actual optimizer.

    Args:
      *args: Arguments for get_slot().
      **kwargs: Keyword arguments for get_slot().

    Returns:
      The `Variable` for the slot if it was created, `None` otherwise.
    """
exit(self._opt.get_slot(*args, **kwargs))
