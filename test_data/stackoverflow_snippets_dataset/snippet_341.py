# Extracted from https://stackoverflow.com/questions/4843158/how-to-check-if-a-string-is-a-substring-of-items-in-a-list-of-strings
a = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
for i in a:
    if i.__contains__("abc") :
        print(i, " is containing")

