# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/choose_from_datasets_test.py
datasets = [
    dataset_ops.Dataset.from_tensors(b"foo").repeat(2),
    dataset_ops.Dataset.from_tensors(b"bar").repeat(),
    dataset_ops.Dataset.from_tensors(b"baz").repeat(),
]
choice_array = np.asarray([0, 0, 0, 1, 1, 1, 2, 2, 2], dtype=np.int64)
choice_dataset = dataset_ops.Dataset.from_tensor_slices(choice_array)
dataset = dataset_ops.Dataset.choose_from_datasets(
    datasets, choice_dataset, stop_on_empty_dataset=False)
# Chooses 2 elements from the first dataset while the selector specifies 3.
self.assertDatasetProduces(
    dataset,
    [b"foo", b"foo", b"bar", b"bar", b"bar", b"baz", b"baz", b"baz"])
