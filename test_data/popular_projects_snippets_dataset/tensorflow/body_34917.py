# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
z = np_func(x, y)
zs = list(z.shape)
with self.cached_session():
    inx = ops.convert_to_tensor(x)
    iny = ops.convert_to_tensor(y)
    if x.dtype in (np.float32, np.float64):
        out = 1.1 * tf_func(inx, iny)
    else:
        out = tf_func(inx, iny)
    xs = list(x.shape)
    jacob_t, jacob_n = gradient_checker.compute_gradient(
        inx, xs, out, zs, x_init_value=x)
    if numeric_gradient_type is not None:
        xf = x.astype(numeric_gradient_type)
        yf = y.astype(numeric_gradient_type)
        inxf = ops.convert_to_tensor(xf)
        inyf = ops.convert_to_tensor(yf)
        outf = tf_func(inxf, inyf)
        _, jacob_n = gradient_checker.compute_gradient(
            inxf, xs, outf, zs, x_init_value=xf, delta=1e-3)
        jacob_n = jacob_n.astype(x.dtype)
    tol = self._GRAD_TOL[dtypes_lib.as_dtype(x.dtype)]
    self.assertAllClose(jacob_t, jacob_n, rtol=tol, atol=tol)
