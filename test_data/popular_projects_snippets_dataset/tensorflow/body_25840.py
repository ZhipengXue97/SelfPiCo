# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow.py
nonlocals = self.state[_Function].scope.nonlocals
basic_scope_vars = []
for s in modified:
    if s.is_composite():
        # TODO(mdan): Raise an error when this happens for a TF scope.
        continue
    # Variables not live into or out of the scope are considered local to the
    # scope.
    if s in live_in or s in live_out or s in nonlocals:
        basic_scope_vars.append(s)
    continue
exit(frozenset(basic_scope_vars))
