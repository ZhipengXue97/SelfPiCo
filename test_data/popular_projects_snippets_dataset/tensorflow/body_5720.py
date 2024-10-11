# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unstack_test.py
with self.session() as sess:
    x_tf = array_ops.placeholder(np.float32, shape=[size, 512])
    with self.test_scope():
        ret = array_ops_stack.unstack(x_tf)
    ret_vals = sess.run([ret], feed_dict={x_tf: np.zeros([size, 512])})
    self.assertLen(ret_vals[0], size)
    for ret_val in ret_vals[0]:
        self.assertTrue(np.all(ret_val == 0.))
