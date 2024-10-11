# Extracted from https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
[{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]

sorted(l,cmp=lambda x,y: cmp(x['name'],y['name']))

