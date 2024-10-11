# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam.py
m = self.get_slot(var, "m")
v = self.get_slot(var, "v")
beta1_power, beta2_power = self._get_beta_accumulators()
exit(training_ops.apply_adam(
    var,
    m,
    v,
    math_ops.cast(beta1_power, var.dtype.base_dtype),
    math_ops.cast(beta2_power, var.dtype.base_dtype),
    math_ops.cast(self._lr_t, var.dtype.base_dtype),
    math_ops.cast(self._beta1_t, var.dtype.base_dtype),
    math_ops.cast(self._beta2_t, var.dtype.base_dtype),
    math_ops.cast(self._epsilon_t, var.dtype.base_dtype),
    grad,
    use_locking=self._use_locking).op)
