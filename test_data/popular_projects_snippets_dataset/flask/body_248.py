# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Like :meth:`before_request`, but before every request, not only those handled
        by the blueprint. Equivalent to :meth:`.Flask.before_request`.
        """
self.record_once(
    lambda s: s.app.before_request_funcs.setdefault(None, []).append(f)
)
exit(f)
