# Extracted from https://stackoverflow.com/questions/16819222/how-do-i-return-dictionary-keys-as-a-list-in-python
some_dict = {1: 'one', 2: 'two', 3: 'three'}
list_of_keys = list(some_dict.keys())
print(list_of_keys)

list_of_keys = []
list_of_values = []
for key,val in some_dict.items():
    list_of_keys.append(key)
    list_of_values.append(val)

print(list_of_keys)

print(list_of_values)

