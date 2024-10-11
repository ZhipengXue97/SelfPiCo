# Extracted from https://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python
listone = [1,2,3]
listtwo = [4,5,6]

listone.extend(listtwo)

mergedlist = []
mergedlist.extend(listone)
mergedlist.extend(listtwo)

