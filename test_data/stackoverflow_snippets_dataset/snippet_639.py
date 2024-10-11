# Extracted from https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
import re
a = input()
b = input()
if b not in a:
    print((-1,-1))
else:
    #create two list as
    start_indc = [m.start() for m in re.finditer('(?=' + b + ')', a)]
    for i in range(len(start_indc)):
        print((start_indc[i], start_indc[i]+len(b)-1))

aaadaa
aa
(0, 1)
(1, 2)
(4, 5)

