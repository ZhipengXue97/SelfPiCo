# Extracted from https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string
a = "I walked today,"
c=['d','e','f']
count=0
for i in a:
    if str(i) in c:
        count+=1

print(count)

