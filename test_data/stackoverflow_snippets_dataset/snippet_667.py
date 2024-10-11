# Extracted from https://stackoverflow.com/questions/3975376/why-updating-shallow-copy-dictionary-doesnt-update-original-dictionary
original = dict(a=1, b=2, c=dict(d=4, e=5))
new = original.copy()

new['a'] = 10
# new = {'a': 10, 'b': 2, 'c': {'d': 4, 'e': 5}}
# original = {'a': 1, 'b': 2, 'c': {'d': 4, 'e': 5}}
# no change in original, since ['a'] is an immutable integer

new['c']['d'] = 40
# new = {'a': 10, 'b': 2, 'c': {'d': 40, 'e': 5}}
# original = {'a': 1, 'b': 2, 'c': {'d': 40, 'e': 5}}
# new['c'] points to the same original['d'] mutable dictionary, so it will be changed

