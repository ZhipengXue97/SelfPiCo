# Extracted from https://stackoverflow.com/questions/15411107/delete-a-dictionary-item-if-the-key-exists
keys_to_remove = set(keys).intersection(set(mydict.keys()))
for key in keys_to_remove:
    del mydict[key]

keys_to_keep = set(mydict.keys()) - set(keys)
new_dict = {k: v for k, v in mydict.iteritems() if k in keys_to_keep}

keys_to_keep = set(mydict.keys()) - set(keys)
new_dict = {k: mydict[k] for k in keys_to_keep}

