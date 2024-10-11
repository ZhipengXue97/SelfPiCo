# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Like :meth:`errorhandler`, but for every request, not only those handled by
        the blueprint. Equivalent to :meth:`.Flask.errorhandler`.
        """

def decorator(f: T_error_handler) -> T_error_handler:
    self.record_once(lambda s: s.app.errorhandler(code)(f))
    exit(f)

exit(decorator)
