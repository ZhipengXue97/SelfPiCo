# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
file1 = self._writeFile("f0", [1, 2, 3])
file2 = self._writeFile("f1", [4, 5, 6])
file3 = self._writeFile("f2", [7, 8, 9])
dataset = dataset_ops.Dataset.from_tensor_slices([file1, file2, file3])
dataset = dataset.map(core_readers.TFRecordDataset)
dataset = dataset.interleave(lambda x: x, cycle_length=3)
dataset = distribute._AutoShardDataset(dataset, 2, 0)

# Sharding by file will interleave files 0 and 2
expected = [str.encode(str(i)) for i in [1, 7, 2, 8, 3, 9]]
actual = self.getDatasetOutput(dataset)
self.assertEqual(actual, expected)
