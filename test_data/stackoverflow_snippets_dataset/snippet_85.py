# Extracted from https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
import itertools
x = itertools.count(0)
type(x).__name__
'count'

x.__class__.__name__

