# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Like :meth:`context_processor`, but for templates rendered by every view, not
        only by the blueprint. Equivalent to :meth:`.Flask.context_processor`.
        """
self.record_once(
    lambda s: s.app.template_context_processors.setdefault(None, []).append(f)
)
exit(f)
