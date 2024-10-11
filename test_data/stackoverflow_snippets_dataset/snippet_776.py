# Extracted from https://stackoverflow.com/questions/4481724/convert-a-list-of-characters-into-a-string
from operator import concat
a = ['a', 'b', 'c', 'd']
reduce(concat, a)
'abcd'

from functools import reduce

