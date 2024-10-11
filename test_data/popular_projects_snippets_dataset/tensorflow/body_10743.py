# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
_assert_in_default_state(self)

def merge_fn(dist, s):
    self.assertIs(distribute_lib._get_default_strategy(), dist)
    self.assertIs(None, distribute_lib.get_replica_context())
    self.assertIs(dist, distribute_lib.get_cross_replica_context())
    self.assertTrue(distribute_lib.in_cross_replica_context())
    self.assertIs(dist, distribute_lib.get_strategy())
    self.assertFalse(distribute_lib.has_strategy())
    exit("foo_" + s)

replica_ctx = distribute_lib.get_replica_context()
self.assertIs(distribute_lib._get_default_replica_context(), replica_ctx)
self.assertEqual("foo_bar", replica_ctx.merge_call(merge_fn, args=("bar",)))
_assert_in_default_state(self)
