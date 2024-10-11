# Extracted from https://stackoverflow.com/questions/306400/how-can-i-randomly-select-an-item-from-a-list
s=set(range(1,6))
import random

while len(s)>0:
  s.remove(random.choice(list(s)))
  print(s)


set([1, 3, 4, 5])
set([3, 4, 5])
set([3, 4])
set([4])
set([])

set([1, 2, 3, 5])
set([2, 3, 5])
set([2, 3])
set([2])
set([])


set([1, 2, 3, 5])
set([1, 2, 3])
set([1, 2])
set([1])
set([])

