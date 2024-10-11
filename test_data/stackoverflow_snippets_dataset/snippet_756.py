# Extracted from https://stackoverflow.com/questions/1585322/is-there-a-way-to-perform-if-in-pythons-lambda
from __future__ import print_function

f = lambda x: print(x) if x%2 == 0 else False

