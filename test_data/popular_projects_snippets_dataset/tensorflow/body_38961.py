# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
# We will test mean, cov, var, stddev on a DirichletMultinomial constructed
# via broadcast between alpha, n.
alpha = np.array([[1., 2, 3],
                  [2.5, 4, 0.01]], dtype=np.float32)
# Ideally we'd be able to test broadcasting but, the multinomial sampler
# doesn't support different total counts.
n = np.float32(5)
with self.cached_session() as sess:
    # batch_shape=[2], event_shape=[3]
    dist = ds.DirichletMultinomial(n, alpha)
    x = dist.sample(int(250e3), seed=1)
    sample_mean = math_ops.reduce_mean(x, 0)
    x_centered = x - sample_mean[array_ops.newaxis, ...]
    sample_cov = math_ops.reduce_mean(math_ops.matmul(
        x_centered[..., array_ops.newaxis],
        x_centered[..., array_ops.newaxis, :]), 0)
    sample_var = array_ops.matrix_diag_part(sample_cov)
    sample_stddev = math_ops.sqrt(sample_var)
    [
        sample_mean_,
        sample_cov_,
        sample_var_,
        sample_stddev_,
        analytic_mean,
        analytic_cov,
        analytic_var,
        analytic_stddev,
    ] = sess.run([
        sample_mean,
        sample_cov,
        sample_var,
        sample_stddev,
        dist.mean(),
        dist.covariance(),
        dist.variance(),
        dist.stddev(),
    ])
    self.assertAllClose(sample_mean_, analytic_mean, atol=0.04, rtol=0.)
    self.assertAllClose(sample_cov_, analytic_cov, atol=0.05, rtol=0.)
    self.assertAllClose(sample_var_, analytic_var, atol=0.05, rtol=0.)
    self.assertAllClose(sample_stddev_, analytic_stddev, atol=0.02, rtol=0.)
