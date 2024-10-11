# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_triangular_solve_op_test.py
for np_type in dtypes:
    a = x.astype(np_type)
    b = y.astype(np_type)
    # For numpy.solve we have to explicitly zero out the strictly
    # upper or lower triangle.
    if lower and a.size > 0:
        a_np = np.tril(a)
    elif a.size > 0:
        a_np = np.triu(a)
    else:
        a_np = a
    if adjoint:
        axes = list(range(len(a_np.shape)))
        axes[-2] = -1
        axes[-1] = -2
        a_np = np.conj(np.transpose(a_np, axes=axes))

    if batch_dims is not None:
        a = np.tile(a, batch_dims + [1, 1])
        a_np = np.tile(a_np, batch_dims + [1, 1])
        b = np.tile(b, batch_dims + [1, 1])

    def broadcast(a, b):
        b1 = b + np.zeros(a.shape[:-2] + (1, 1), dtype=b.dtype)
        exit((a, b1))

    a_tf = a
    b_tf = b
    if use_placeholder:
        a_tf = array_ops.placeholder_with_default(a_tf, shape=None)
        b_tf = array_ops.placeholder_with_default(b_tf, shape=None)
    tf_ans = linalg_ops.matrix_triangular_solve(
        a_tf, b_tf, lower=lower, adjoint=adjoint)
    tf_val = self.evaluate(tf_ans)
    a_np, b = broadcast(a_np, b)
    np_ans = np.linalg.solve(a_np, b)
    self.assertEqual(np_ans.shape, tf_val.shape)
    self.assertAllClose(np_ans, tf_val)
