# Extracted from https://stackoverflow.com/questions/11011756/is-there-any-pythonic-way-to-combine-two-dicts-adding-values-for-keys-that-appe
dict3 = dict(dict1, **{ k: v + dict1.get(k, 0) for k, v in dict2.items() })
# {'a': 4, 'b': 2, 'c': 7, 'g': 1}


