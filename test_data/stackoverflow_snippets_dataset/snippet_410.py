# Extracted from https://stackoverflow.com/questions/15478127/remove-final-character-from-string
s = "abcd"
s[:3]
'abc'

s = "abcd"
s[:-1]
'abc'

s = "abcd"
s[:len(s) - 1]
'abc'

