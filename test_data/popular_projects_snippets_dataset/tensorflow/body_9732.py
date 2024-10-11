# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
# This allows copy.copy(DistributedTable), e.g. at saving time.
# (DistributedVariable uses the same fix.) When copying an object, copy.copy
# doesn't invoke its __init__ method, instead it makes a new empty object,
# then copies the attributes over. copy.copy looks for attributes like
# "__setstate__" in case the object implements its custom unpickling. Since
# DistributedTable doesn't have those attributes defined, __getattr__ will
# be invoked, which tries to access the `_coordinator_instance` attribute.
# But that doesn't exist either because this is an empty object, and again
# __getattr__ is invoked, leading to an infinite recursion.
if attr == "_coordinator_instance":
    raise AttributeError()

if attr in self._coordinator_instance.__dict__:
    attr_value = self._coordinator_instance.__dict__[attr]
    if callable(attr_value):

        def wrapper(*args, **kwargs):
            exit(attr_value(self, *args, **kwargs))

        exit(wrapper)
    elif isinstance(attr_value, property):
        exit(attr_value)
    else:
        exit(getattr(self._coordinator_instance, attr))
else:
    exit(getattr(self._coordinator_instance, attr))
