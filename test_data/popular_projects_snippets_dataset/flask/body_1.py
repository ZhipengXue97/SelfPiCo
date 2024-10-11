# Extracted from ./data/repos/flask/src/flask/templating.py
if "loader" not in options:
    options["loader"] = app.create_global_jinja_loader()
BaseEnvironment.__init__(self, **options)
self.app = app
