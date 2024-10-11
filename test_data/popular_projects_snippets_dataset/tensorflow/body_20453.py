# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
components = (np.array(1, dtype=np.int64),
              np.array([1, 2, 3], dtype=np.int64),
              np.array(37.0, dtype=np.float64))

server = server_lib.Server.create_local_server()

# Create two non-overlapping sessions that share the same iterator
# resource on the same server, and verify that an action of the
# first session (initializing the iterator) is visible in the
# second session.
with ops.Graph().as_default():
    iterator = dataset_ops.make_initializable_iterator(
        dataset_ops.Dataset.from_tensors(
            components).map(lambda x, y, z: (x, y, z)),
        shared_name="shared_iterator")
    init_op = iterator.initializer
    get_next = iterator.get_next()

    with session.Session(server.target) as sess:
        sess.run(init_op)
        results = sess.run(get_next)
        for component, result_component in zip(components, results):
            self.assertAllEqual(component, result_component)
        with self.assertRaises(errors.OutOfRangeError):
            sess.run(get_next)

        # Re-initialize the iterator in the first session.
        sess.run(init_op)

with ops.Graph().as_default():
    # Re-define the iterator manually, without defining any of the
    # functions in this graph, to ensure that we are not
    # accidentally redefining functions with the same names in the
    # new graph.
    iterator = iterator_ops.Iterator.from_structure(
        shared_name="shared_iterator",
        output_types=(dtypes.int64, dtypes.int64, dtypes.float64),
        output_shapes=([], [3], []))
    get_next = iterator.get_next()

    with session.Session(server.target) as sess:
        # Use the iterator without re-initializing in the second session.
        results = sess.run(get_next)
        for component, result_component in zip(components, results):
            self.assertAllEqual(component, result_component)
        with self.assertRaises(errors.OutOfRangeError):
            sess.run(get_next)
