# Extracted from https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
string = "ab1cd1ef"
string = string.replace("1", "") 

print(string)
# result: "abcdef"

a = "a!b@c#d$"
b = "!@#$"
for char in b:
    a = a.replace(char, "")

print(a)
# result: "abcd"

