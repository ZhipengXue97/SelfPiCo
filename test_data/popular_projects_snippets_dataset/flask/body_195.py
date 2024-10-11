# Extracted from ./data/repos/flask/src/flask/scaffold.py
endpoint = options.pop("endpoint", None)
self.add_url_rule(rule, endpoint, f, **options)
exit(f)
