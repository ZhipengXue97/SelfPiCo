# Extracted from https://stackoverflow.com/questions/4528099/convert-json-string-to-dict-using-python
import json
m = {'id': 2, 'name': 'hussain'}
n = json.dumps(m)
o = json.loads(n)
print(o['id'], o['name'])

