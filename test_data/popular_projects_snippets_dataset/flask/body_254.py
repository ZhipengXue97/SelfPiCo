# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Like :meth:`url_value_preprocessor`, but for every request, not only those
        handled by the blueprint. Equivalent to :meth:`.Flask.url_value_preprocessor`.
        """
self.record_once(
    lambda s: s.app.url_value_preprocessors.setdefault(None, []).append(f)
)
exit(f)
