# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Like :meth:`teardown_request`, but after every request, not only those
        handled by the blueprint. Equivalent to :meth:`.Flask.teardown_request`.
        """
self.record_once(
    lambda s: s.app.teardown_request_funcs.setdefault(None, []).append(f)
)
exit(f)
