# Extracted from https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
sorted([(value,key) for (key,value) in mydict.items()])

sorted((value,key) for (key,value) in mydict.items())

