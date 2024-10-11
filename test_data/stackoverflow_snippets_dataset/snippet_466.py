# Extracted from https://stackoverflow.com/questions/464864/get-all-possible-2n-combinations-of-a-list-s-elements-of-any-length
flag = 0
requiredCals =12
from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)  # allows duplicate elements
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

stuff = [2,9,5,1,6]
for i, combo in enumerate(powerset(stuff), 1):
    if(len(combo)>0):
        #print(combo , sum(combo))
        if(sum(combo)== requiredCals):
            flag = 1
            break
if(flag==1):
    print('True')
else:
    print('else')


