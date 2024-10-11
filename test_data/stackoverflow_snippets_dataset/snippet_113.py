# Extracted from https://stackoverflow.com/questions/44834/what-does-all-mean-in-python
__all__ = ['bar', 'baz']

waz = 5
bar = 10
def baz(): return 'baz'

from foo import *

print(bar)
print(baz)

# The following will trigger an exception, as "waz" is not exported by the module
print(waz)

