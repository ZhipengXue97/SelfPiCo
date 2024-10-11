# Extracted from https://stackoverflow.com/questions/209840/how-can-i-make-a-dictionary-dict-from-separate-lists-of-keys-and-values
import pprint

p = ['A', 'B', 'C']
q = [5, 2, 7]
r = ["M", "F", "M"]
s = ['Sovabazaar','Shyambazaar','Bagbazaar','Hatkhola']


def makeDictUsingAlternateLists1(**rest):
    print("*rest.keys() : ",*rest.keys())
    print("rest.keys() : ",rest.keys())
    print("*rest.values() : ",*rest.values())
    print("**rest.keys() : ",rest.keys())
    print("**rest.values() : ",rest.values())
    [print(a) for a in zip(*rest.values())]
    
    [ print(dict(zip(rest.keys(),a))) for a in zip(*rest.values())]
    print("...")
    
    
    finalRes= [ dict( zip( rest.keys(),a))  for a in zip(*rest.values())] 
    return finalRes
    
l = makeDictUsingAlternateLists1(p=p,q=q,r=r,s=s)
pprint.pprint(l)    
"""
rest.keys() :  dict_keys(['p', 'q', 'r', 's'])
('A', 5, 'M', 'Sovabazaar')
('B', 2, 'F', 'Shyambazaar')
('C', 7, 'M', 'Bagbazaar')
{'p': 'A', 'q': 5, 'r': 'M', 's': 'Sovabazaar'}
{'p': 'B', 'q': 2, 'r': 'F', 's': 'Shyambazaar'}
{'p': 'C', 'q': 7, 'r': 'M', 's': 'Bagbazaar'}
[{'p': 'A', 'q': 5, 'r': 'M', 's': 'Sovabazaar'},
 {'p': 'B', 'q': 2, 'r': 'F', 's': 'Shyambazaar'},
 {'p': 'C', 'q': 7, 'r': 'M', 's': 'Bagbazaar'}]
 
"""

