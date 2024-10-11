# Extracted from https://stackoverflow.com/questions/3697432/how-to-find-list-intersection
from collections import Counter
a = [1,2,3,4,5]
b = [1,3,5,6]
d1, d2 = Counter(a), Counter(b)
c = [n for n in d1.keys() & d2.keys() for _ in range(min(d1[n], d2[n]))]
print(c)
[1,3,5]

