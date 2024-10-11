# Extracted from https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
list1 = ["hello", " ", "w", "o", "r", "l", "d"]
sorted(set(list1 ), key=list1.index)

["hello", " ", "w", "o", "r", "l", "d"]

