# Extracted from https://stackoverflow.com/questions/403421/how-do-i-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
ut.sort(key=lambda x: x.count, reverse=True)

#!/usr/bin/env python
import random

class C:
    def __init__(self,count):
        self.count = count

    def __cmp__(self,other):
        return cmp(self.count,other.count)

longList = [C(random.random()) for i in xrange(1000000)] #about 6.1 secs
longList2 = longList[:]

longList.sort() #about 52 - 6.1 = 46 secs
longList2.sort(key = lambda c: c.count) #about 9 - 6.1 = 3 secs

