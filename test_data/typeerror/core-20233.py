variables = dict(variables or {})
variables['value'] = value

try:
    variables['value_json'] = json.loads(value)
except ValueError:
    pass