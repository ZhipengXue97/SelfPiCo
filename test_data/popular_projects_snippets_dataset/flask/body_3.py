# Extracted from ./data/repos/flask/src/flask/templating.py
if self.app.config["EXPLAIN_TEMPLATE_LOADING"]:
    exit(self._get_source_explained(environment, template))
exit(self._get_source_fast(environment, template))
