# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Utility to initialize uninitialized variables on the fly."""
variables = _get_variables(get_graph())
candidate_vars = []
for v in variables:
    if not getattr(v, '_keras_initialized', False):
        candidate_vars.append(v)
if candidate_vars:
    # This step is expensive, so we only run it on variables not already
    # marked as initialized.
    is_initialized = session.run(
        [variable_v1.is_variable_initialized(v) for v in candidate_vars])
    # TODO(kathywu): Some metric variables loaded from SavedModel are never
    # actually used, and do not have an initializer.
    should_be_initialized = [
        (not is_initialized[n]) and v.initializer is not None
        for n, v in enumerate(candidate_vars)]
    uninitialized_vars = []
    for flag, v in zip(should_be_initialized, candidate_vars):
        if flag:
            uninitialized_vars.append(v)
        v._keras_initialized = True
    if uninitialized_vars:
        session.run(variables_module.variables_initializer(uninitialized_vars))
