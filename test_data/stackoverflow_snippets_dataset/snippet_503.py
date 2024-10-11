# Extracted from https://stackoverflow.com/questions/577234/python-extend-for-a-dictionary
from collections import ChainMap
c = ChainMap(a, b)
c['a'] # returns 1

