# Extracted from ./data/repos/flask/src/flask/templating.py
result = set()
loader = self.app.jinja_loader
if loader is not None:
    result.update(loader.list_templates())

for blueprint in self.app.iter_blueprints():
    loader = blueprint.jinja_loader
    if loader is not None:
        for template in loader.list_templates():
            result.add(template)

exit(list(result))
