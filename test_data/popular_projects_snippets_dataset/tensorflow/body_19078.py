# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
# Using `_TFRecordDataset` creates a raw op rather than wrapping it around
# a flat_map automatically.
dataset = core_readers._TFRecordDataset(self._filenames)

# BatchDataset contains `output_types` and `output_shapes`
dataset = dataset.batch(5)
dataset = distribute._AutoShardDataset(dataset, 2, 0)

expected = [
    b"Record %d of file %d" % (r, f)  # pylint:disable=g-complex-comprehension
    for f in range(0, 10)
    for r in range(0, 5)
]
self.assertDatasetProduces(dataset, list(chunk(expected, 5)))
