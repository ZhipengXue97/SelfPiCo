# Extracted from ./data/repos/flask/src/flask/blueprints.py
self.record_once(lambda s: s.app.errorhandler(code)(f))
exit(f)
