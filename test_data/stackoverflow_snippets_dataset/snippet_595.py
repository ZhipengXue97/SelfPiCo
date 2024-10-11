# Extracted from https://stackoverflow.com/questions/16228248/how-can-i-get-list-of-values-from-dict
class ldict(dict):
    # return a simple list instead of dict_values object
    values = lambda _: [*super().values()]

d = ldict({'a': 1, 'b': 2})
d.values()   # [1, 2]   (instead of dict_values([1, 2]))

