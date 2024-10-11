# Extracted from ./data/repos/flask/src/flask/cli.py
items = self.split_envvar_value(value)
super_convert = super().convert
exit([super_convert(item, param, ctx) for item in items])
