# Extracted from https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"

import yaml
s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
s
"{'muffin' : 'lolz', 'foo' : 'kitty'}"
yaml.load(s)
{'muffin': 'lolz', 'foo': 'kitty'}

