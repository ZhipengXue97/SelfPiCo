# Extracted from https://stackoverflow.com/questions/3462143/get-difference-between-two-lists-with-unique-entries
list(set(x).symmetric_difference(set(y)))
list(set(x) ^ set(y))

import time
import random
from itertools import filterfalse

# 1 - performance (time taken)
# 2 - correctness (answer - 1,4,5,6)
# set performance
performance = 1
numberoftests = 7

def answer(x,y,z):
    if z == 0:
        start = time.clock()
        lists = (str(list(set(x)-set(y))+list(set(y)-set(y))))
        times = ("1 = " + str(time.clock() - start))
        return (lists,times)

    elif z == 1:
        start = time.clock()
        lists = (str(list(set(x).symmetric_difference(set(y)))))
        times = ("2 = " + str(time.clock() - start))
        return (lists,times)

    elif z == 2:
        start = time.clock()
        lists = (str(list(set(x) ^ set(y))))
        times = ("3 = " + str(time.clock() - start))
        return (lists,times)

    elif z == 3:
        start = time.clock()
        lists = (filterfalse(set(y).__contains__, x))
        times = ("4 = " + str(time.clock() - start))
        return (lists,times)

    elif z == 4:
        start = time.clock()
        lists = (tuple(set(x) - set(y)))
        times = ("5 = " + str(time.clock() - start))
        return (lists,times)

    elif z == 5:
        start = time.clock()
        lists = ([tt for tt in x if tt not in y])
        times = ("6 = " + str(time.clock() - start))
        return (lists,times)

    else:    
        start = time.clock()
        Xarray = [iDa for iDa in x if iDa not in y]
        Yarray = [iDb for iDb in y if iDb not in x]
        lists = (str(Xarray + Yarray))
        times = ("7 = " + str(time.clock() - start))
        return (lists,times)

n = numberoftests

if performance == 2:
    a = [1,2,3,4,5]
    b = [3,2,6]
    for c in range(0,n):
        d = answer(a,b,c)
        print(d[0])

elif performance == 1:
    for tests in range(0,10):
        print("Test Number" + str(tests + 1))
        a = random.sample(range(1, 900000), 9999)
        b = random.sample(range(1, 900000), 9999)
        for c in range(0,n):
            #if c not in (1,4,5,6):
            d = answer(a,b,c)
            print(d[1])

