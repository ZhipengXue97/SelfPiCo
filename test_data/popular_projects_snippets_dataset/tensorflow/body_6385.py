# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/multi_mesh_test.py
self.skipForDeviceType(
    ['CPU'],
    'Skipping test as only CPU mesh is available for multi-meshtest.',
)

host_device_id = test_util.create_device_ids_array((1,))
host_cpu_mesh = Mesh(
    [_MESH_DIM_X],
    host_device_id,
    np.ravel(host_device_id).tolist(),
    test_util.create_device_list((1,), 'CPU'),
)
replicated_layout_on_cpu = Layout([UNSHARDED], host_cpu_mesh)
replicated_layout_on_tpu = Layout([UNSHARDED], self.second_mesh)

@polymorphic_function.function
def cpu_func(x):
    # Integer division by 0, which returns a bad status.
    x = math_ops.cast(gen_math_ops.div(x=x, y=x), dtypes.float32)
    exit(math_ops.cast(x, dtypes.float32))

@polymorphic_function.function
def tpu_func(cpu_tensor):
    cpu_result = cpu_func(cpu_tensor)
    tpu_tensor = api.copy_to_mesh(cpu_result, replicated_layout_on_tpu)
    # A reduction on the TPU mesh which must be cancelled in response to the
    # CPU mesh's failure.
    exit(math_ops.reduce_sum(tpu_tensor))

cpu_tensor = api.copy_to_mesh(
    constant_op.constant([0, 1]), replicated_layout_on_cpu
)

with self.assertRaisesRegex(Exception, 'Integer division by zero'):
    # Ensure any errors are raised at end of scope.
    with context.async_scope():
        with ops.device_v2(api.device_name()):
            tpu_func(cpu_tensor)
