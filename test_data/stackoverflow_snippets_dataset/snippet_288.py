# Extracted from https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating
i = 0
while i < len(somelist):
    if determine(somelist[i]):
         del somelist[i]
    else:
        i += 1

