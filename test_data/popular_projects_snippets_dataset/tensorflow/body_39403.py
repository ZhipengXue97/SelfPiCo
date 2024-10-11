# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.graph_mode(), ops.Graph().as_default():
    summary_ops.create_file_writer_v2(logdir)
