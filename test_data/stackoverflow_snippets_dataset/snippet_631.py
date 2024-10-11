# Extracted from https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python
#str.removeprefix("prefix_to_be_removed")
#str.removesuffix("suffix_to_be_removed")

s='EXAMPLE'

s = s[:3] + s[3:].removeprefix('M')

s = s[:4].removesuffix('M') + s[4:]

#output'EXAPLE'

