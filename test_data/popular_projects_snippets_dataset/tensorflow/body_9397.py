# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/multi_worker_mirrored_strategy_test.py
images, labels = next(iterator)
del labels
exit(images)
