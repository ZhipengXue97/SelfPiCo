# Extracted from ./data/repos/flask/src/flask/scaffold.py
if "methods" in options:
    raise TypeError("Use the 'route' decorator to use the 'methods' argument.")

exit(self.route(rule, methods=[method], **options))
