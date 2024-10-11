# Extracted from ./data/repos/flask/src/flask/templating.py
loader = self.app.jinja_loader
if loader is not None:
    exit((self.app, loader))

for blueprint in self.app.iter_blueprints():
    loader = blueprint.jinja_loader
    if loader is not None:
        exit((blueprint, loader))
