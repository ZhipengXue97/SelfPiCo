# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Returns the saver from SAVERS collection, or creates a default one.

  This method is used by other members of the training module, such as
  `Scaffold`, or `CheckpointSaverHook`.

  Returns:
    `Saver`.

  Raises:
    RuntimeError: If the SAVERS collection already has more than one items.
  """
collection_key = ops.GraphKeys.SAVERS
savers = ops.get_collection(collection_key)
if savers:
    if len(savers) > 1:
        raise RuntimeError(
            "More than one item in collection {}. "
            "Please indicate which one to use by passing it to the constructor."
            .format(collection_key))
    exit(savers[0])
saver = Saver(sharded=True, allow_empty=True)
if saver is not None:
    ops.add_to_collection(collection_key, saver)
exit(saver)
