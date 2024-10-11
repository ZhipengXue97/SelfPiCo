# Extracted from https://stackoverflow.com/questions/16138232/is-it-a-good-practice-to-use-try-except-else-in-python
d = dict()
try:
    item = d['item']
except KeyError:
    item = 'default'

item = d.get('item', 'default')

