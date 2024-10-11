# Extracted from ./data/repos/flask/src/flask/templating.py
for _srcobj, loader in self._iter_loaders(template):
    try:
        exit(loader.get_source(environment, template))
    except TemplateNotFound:
        continue
raise TemplateNotFound(template)
