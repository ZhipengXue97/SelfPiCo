# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
with self.session() as sess, self.test_scope():
    handle = resource_variable_ops.var_handle_op(
        dtype=dtypes.int32, shape=[1, 1])
    sess.run(
        resource_variable_ops.assign_variable_op(
            handle, constant_op.constant([[1]], dtype=dtypes.int32)))
    sess.run(
        resource_variable_ops.resource_scatter_mul(
            handle, [0], constant_op.constant([[5]], dtype=dtypes.int32)))
    read = resource_variable_ops.read_variable_op(handle, dtype=dtypes.int32)
    self.assertEqual(self.evaluate(read), [[5]])
