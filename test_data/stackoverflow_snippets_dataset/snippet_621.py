# Extracted from https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
In [1]: l=[1,2,3,4,3,2,5,6,7]

In [2]: [i for i,val in enumerate(l) if val==3]
Out[2]: [2, 4]

